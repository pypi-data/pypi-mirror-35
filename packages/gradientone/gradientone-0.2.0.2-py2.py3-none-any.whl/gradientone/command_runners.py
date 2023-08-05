"""

Copyright (C) 2016-2017 GradientOne Inc. - All Rights Reserved
Unauthorized copying or distribution of this file is strictly prohibited
without the express permission of GradientOne Inc.

"""

import collections
import pickle
import os
from os import remove

import gateway_helpers
import multiprocessing as multi
import tek_grl_configs
import time
import traceback
import usb
import utilization
from configparser import ConfigParser
from copy import deepcopy
from json import dumps, loads
from datetime import datetime

from os.path import exists

from gradientone.base import BaseClient, COMMAND_FILENAME
# from gradientone.device_drivers.can.CANcard import CanFrame, CmdErr
# from gradientone.device_drivers.can.can_headers import registers
# from gradientone.device_drivers.can.can_helpers import interpret_expression
# from gradientone.device_drivers.can.motor import Motor
from gradientone.gateway_helpers import get_headers, post_config_form
from misc_transformers import TransformerGRLTest
from re import match, sub
from transformers import (
    Transformer, ScopeTransformer, TransformerMSO2302A, TransformerMSO5204B,
    TransformerMSO2024, TransformerMDO3012, TransformerDS1054Z,
    TransformerDPO3014, TransformerDPO3034, TransformerMDO4104,
)
from transmitters import (
    CANOpenTransmitter, ScopeTransmitter, GRLTransmitter,
)
try:
    from urllib.parse import urljoin
except:
    from urlparse import urljoin


cfg = ConfigParser()
cfg.read('/etc/gradient_one.cfg')
COMMON_SETTINGS = cfg['common']
CLIENT_SETTINGS = cfg['client']


SENTRY_CLIENT = gateway_helpers.get_sentry()

if COMMON_SETTINGS["DOMAIN"].find("localhost") == 0 or COMMON_SETTINGS["DOMAIN"].find("127.0.0.1") == 0:  # noqa
    BASE_URL = "http://" + COMMON_SETTINGS["DOMAIN"]
else:
    BASE_URL = "https://" + COMMON_SETTINGS["DOMAIN"]

CLIENT_ID = 'ORIGINAL'
SAMPLE_FILE = 'MDO30121M.txt'
CONFIG_URL = (BASE_URL, '/testplansummary/' +
              COMMON_SETTINGS['COMPANYNAME'] + '/' +
              COMMON_SETTINGS['HARDWARENAME'])
DEFAULT_TEK_TYPE = 'TektronixMDO3012'

# Careful! Setting BREATH_TIME any lower can cause issues.
# The 'instance hours' issue can happen by repeatedly
# making 100 requests per second and every second.
# HTTPS requests don't work that quickly anyway,
# so going lower than 0.25 is a waste of bandwidth
BREATH_TIME = 0.25
MAX_RETRIES = 5

CANBUS_URL = urljoin(BASE_URL, "motor/canbus")

logger = gateway_helpers.logger


class CommandRunner(BaseClient):

    """CommandRunner runs the 'test' instructions form the server

       Note that a 'test' is not always an actual pass/fail test,
       the 'test' could be a configured scope waveform trace, or
       just a powermeter reading, or instructions for a motor, etc.

       run_command - this is the top level function that gets
                       when the client code creates a command
       single_run - most test runs will call this for a single run
       get_trace - when a trace is needed from the instrument,
                   this uses a Transformer for the instrument
                   to pass instructions and get the trace data,
                   then returns a Transmitter to send to server
    """

    def __init__(self, *args, **kwargs):
        super(CommandRunner, self).__init__(*args, **kwargs)
        self._command = None
        self.setup = None  # setup is being deprecated for 'command' property

        # Timer sets and clears the timeouts
        self.timer = gateway_helpers.Timer()
        # the connection to the copley card
        self.card = None
        self.logger = logger

    @property
    def command(self):
        self._command = collections.defaultdict(str)
        if self.setup:
            self._command.update(self.setup)
        return self._command

    def run_command(self, command):
        self.setup = command  # setup is being deprecated for 'command'
        # update command status to 'in progress'
        data = {
            'status': 'in progress',
            'command_id': command['id']
        }
        logger.info("Updating %s to a %s status"
                    % (command['id'], data['status']))
        response = self.put(BASE_URL + '/commands', data=dumps(data))
        assert response.status_code == 200

        trace = None
        if self.command['label'] == 'GRL':
            self.run_grl_test()
        elif command['category'] in ['Capture', 'Config']:
            trace = self.get_trace()
        elif "frames" in command["info"]:
            # we don't care about the trace
            trace = self.get_trace()
        elif self.command['label'] == 'reset_usb_device':
            gateway_helpers.reset_device_with_tag(command['device_tag'])
        else:
            logger.warning("command with no control commands:" +
                           str(self.command["id"]))
        if trace:
            if trace.metadata["result_id"] != 0:
                logger.info("got trace: %s from command %s" % (trace, self.command))
                transmit_ps = multi.Process(target=trace.transmit_trace,
                                            name='nanny_process:' +
                                                 COMMON_SETTINGS['DOMAIN'])
                transmit_ps.start()

    def run_grl_test(self):
        grl = tek_grl_configs.Grl_Test()
        grl.run_grl_test()

    def gen_data(self):
        command_id = self.setup["id"]
        if command_id == 0:
            raise ValueError("Test run id is zero! Setup is:" + str(
                self.setup))
        return {"command_id": command_id}

    def _get_instrument(self):
        self.timer.set_timeout(30)
        instr = None
        try:
            logger.debug("getting instrument")
            instr = gateway_helpers.get_instrument(self.command['info'])
        except usb.core.USBError:
            logger.debug("USBError!")
            # reset and retry
            gateway_helpers.reset_device_with_tag()
            time.sleep(1)
            instr = gateway_helpers.get_instrument(self.command['info'])
        except Exception:
            logger.warning("Failed to get instrument instance", exc_info=True)
            SENTRY_CLIENT.captureException()
        self.timer.clear_timeout()
        if not instr:
            logger.warning("No instrument available for trace")
            return None
        return instr

    def _get_transformer(self, instr=None):
        command = self.command
        i_transformer = None
        try:
            info = collections.defaultdict(str, command['info'])
            logger.info("Getting transformer for %s" % info['instrument_type'])
            if info['instrument_type'] == 'TektronixMSO2024':
                i_transformer = TransformerMSO2024(command, instr)
            elif info['instrument_type'] == 'TektronixMDO3012':
                i_transformer = TransformerMDO3012(command, instr)
            elif info['instrument_type'] == 'RigolMSO2302A':
                i_transformer = TransformerMSO2302A(command, instr)
            elif info['instrument_type'] == 'RigolDS1054Z':
                i_transformer = TransformerDS1054Z(command, instr)
            elif info['instrument_type'] == 'TektronixMSO5204B':
                i_transformer = TransformerMSO5204B(command, instr)
            elif info['instrument_type'] == 'TektronixDPO3014':
                i_transformer = TransformerDPO3014(command, instr)
            elif info['instrument_type'] == 'TektronixDPO3034':
                i_transformer = TransformerDPO3034(command, instr)
            elif info['instrument_type'] == 'TektronixMDO4104':
                i_transformer = TransformerMDO4104(command, instr)
            elif info['instrument_type'] == 'GenericScope':
                i_transformer = ScopeTransformer(command, instr)
            elif info['g1_measurement'] == 'grl_test':
                i_transformer = TransformerGRLTest(command, instr)
            else:
                i_transformer = Transformer(command, instr)
        except Exception:
            logger.debug("unable to build transformer... no trace")
            logger.debug("closing intrument without receiving trace")
            if instr:
                instr.close()
            logger.debug(traceback.format_exc())
            SENTRY_CLIENT.captureException()
        return i_transformer

    def _get_transmitter(self, i_transformer=None, trace_data=None):
        if not trace_data:
            return CANOpenTransmitter()
        try:
            if trace_data['command']['g1_measurement'] == 'grl_test':
                return GRLTransmitter(i_transformer, trace_data)
            else:
                return ScopeTransmitter(i_transformer, trace_data)
        except TypeError:
            return ScopeTransmitter(i_transformer, trace_data)
        except KeyError:
            return ScopeTransmitter(i_transformer, trace_data)
        except Exception:
            logger.debug("Unexpected exception in getting transmitter")
            return None

    def update_instrument_status(self, status):
        try:
            instrument_type = self.command['info']['instrument_type']
        except Exception:
            logger.warning("No instrument_type to update status for")
            return
        instrument_state = {
            'instrument_type': instrument_type,
            'status': status
        }
        self.update_gateway_state({'instruments': [instrument_state]})

    def get_trace(self):
        """ Gets a trace from the instrument.

            This uses a Transformer for the instrument to pass
            instructions and get the trace data, then returns a
            trace object. The trace object is an instance of
            Transmitter that transmits the trace results and test
            run related data. By default it will retry once in case
            it fails on the first try.
        """
        logger.debug("get_trace() called")
        # obtain instrument for trace
        instr = self._get_instrument()
        if not instr:
            return
        utilization.record_start()
        self.update_instrument_status(status="Busy")
        # get transformer for instrument
        i_transformer = self._get_transformer(instr)
        if not i_transformer:
            logger.error("Unable to get i_transformer. Closing instrument")
            instr.close()
            return

        # get trace from instrument by running setup with transformer
        trace = None
        try:
            logger.info("Running trace setup")
            trace = self.process_transformer(i_transformer)
            logger.info("Process_transformer complete")
        except KeyError:
            logger.warning("KeyError in running setup", exc_info=True)
            SENTRY_CLIENT.captureException()
            # no retry on key errors
        except Exception:
            logger.error("Run config failed. Unexpected error", exc_info=True)
            SENTRY_CLIENT.captureException()
            # unexpected error, try again
            logger.info("Retrying to transformer processing", exc_info=True)
            trace = self.process_transformer(i_transformer)
            self.update_commands(status='failed')
        finally:
            logger.info("Instrument processing complete, closing connection")
            instr.close()
            utilization.record_end()
            self.update_instrument_status(status="Ready")
            if os.path.exists(COMMAND_FILENAME):
                command = pickle.load(open(COMMAND_FILENAME, "r"))
                if "result_id" not in command:
                    command["result_id"] = None
                i_url = BASE_URL + "/instructions.json"
                logger.info("result id get_trace %s" % command["result_id"])
                instruction_data = {
                    "command_metadata": True,
                    'instruction_id': command['instruction_id'],
                    'result_id': command["result_id"],
                    'command_id': command["id"],
                    'duration': (
                    datetime.now() - command['start_datetime']).total_seconds()
                }
                response = self.put(i_url, data=dumps(instruction_data))
                os.remove(COMMAND_FILENAME)
            return trace

    def get_initial_excerpt(self, i_transformer):
        """Returns the intial config excerpt from instrument

        It's important to call this before fetching measurements.
          1) It initializes the instrument and syncs up transformer
          2) It gets an initial state, which is good for debugging

        i_transformer: object that reads back the appropriate
                       fields for the instrument type

        """
        self.timer.set_timeout(240)
        initial_excerpt = None
        try:
            initial_excerpt = i_transformer.get_config_excerpt()
            msg = "initial config setup from instrument: %s" % initial_excerpt
            logger.debug(msg)
        except usb.core.USBError as e:
            logger.debug("USBError!")
            i_transformer.handle_usb_error(e)
        except Exception:
            logger.debug("exception in config_excerpt initialization")
            SENTRY_CLIENT.captureException()
        self.timer.clear_timeout()
        return initial_excerpt

    def load_config(self, i_transformer, trace_dict):
        """loads config to instrument"""
        command = self.command
        success = False
        if command['category'] == 'Capture' or command['category'] == 'Autoset':  # noqa
            logger.debug("measuring without loading config")
            trace_dict['config_name'] = str(command['id'])
            success = i_transformer.check_any_channel_enabled()
        elif "frames" in command["info"]:
            i_transformer.config = command
            i_transformer.load_config()
            success = True
        else:
            trace_dict['config_name'] = self.config['name']
            self.timer.set_timeout(60)
            try:
                success = i_transformer.load_config()
            except usb.core.USBError as e:
                logger.debug("USBError!")
                i_transformer.handle_usb_error(e)
            except Exception:
                logger.debug("Exception in calling load_config()")
                logger.debug(traceback.format_exc())
                SENTRY_CLIENT.captureException()
            self.timer.clear_timeout()
        return success

    def get_meas_dict(self, i_transformer):
        logger.debug("initiate measurement")
        meas_dict = collections.defaultdict(str)
        i_transformer.instr.measurement.initiate()
        self.timer.set_timeout(300)
        try:
            meas_dict = i_transformer.fetch_measurements()
        except usb.core.USBError as e:
            logger.debug("USBError Fetching measurments")
            i_transformer.handle_usb_error(e)
        except Exception:
            logger.debug("fetch_measurements exception")
            logger.debug(traceback.format_exc())
            SENTRY_CLIENT.captureException()
        self.timer.clear_timeout()
        return meas_dict

    def get_metadata(self, i_transformer):
        metadata = collections.defaultdict(str)
        metadata.update(i_transformer.trace_dict)
        self.timer.set_timeout(120)
        try:
            # instrument fetch_setup dump
            metadata['raw_setup'] = i_transformer.fetch_raw_setup()
            # read instrument using ivi fields
            metadata['config_excerpt'] = i_transformer.get_config_excerpt()
        except Exception:
            logger.warning("post-trace fetch config exception", exc_info=True)
            metadata['raw_setup'] = collections.defaultdict(str)
            metadata['config_excerpt'] = collections.defaultdict(str)
            SENTRY_CLIENT.captureException()
        self.timer.clear_timeout()
        i_transformer.times['complete'] = time.time()
        i_transformer.update_scorecard_times()
        return metadata

    def update_with_command_info(self, trace_dict, command):
        trace_dict['test_plan'] = command['test_plan']
        trace_dict['command_id'] = command['id']
        trace_dict['instrument_type'] = command['info']['instrument_type']
        trace_dict['g1_measurement'] = command['g1_measurement']
        return trace_dict

    def process_transformer(self, i_transformer):
        """Runs the setup on the instrument to get trace with measurments

        Called by get_trace(), this function processes transformer to
        collect instrument data, including measurements, config, and
        other metadata. These make up a trace_dict that is passed to
        the Transmitter constructor.

            i_transformer: Transfomer object being processed. This is used
                           to build a trace_dict to then use for the
                           Transmitter contructor.

        Returns a Transmitter object to transmit the trace
        """
        if not i_transformer:
            logger.error("No transformer to process!")
            return
        command = self.command
        command.update(i_transformer.command)
        trace_dict = collections.defaultdict(str)
        self.config = i_transformer.config
        logger.debug("config in setup is: %s" % self.config)
        # sets the ivi usb timeout
        i_transformer.instr._interface.timeout = 25000
        # check for special grl_test
        if command['g1_measurement'] == 'grl_test':
            trace_dict['config_name'] = self.config['name']
            i_transformer.start_test()
            trace_dict['meas_dict'] = collections.defaultdict(str)
        else:
            trace_dict['initial_excerpt'] = self.get_initial_excerpt(
                i_transformer)  # noqa
            logger.info("loading config")
            success = self.load_config(i_transformer, trace_dict)
            if not success:
                msg = "Unable to load config! No measurement collected"
                logger.warning(msg)
                return
            if "frames" not in command["info"]:
                trace_dict['meas_dict'] = self.get_meas_dict(i_transformer)
        # update with transformer dict
        trace_dict.update(i_transformer.trace_dict)
        # update with command info, with priority over transformer
        self.update_with_command_info(trace_dict, command)
        if "frames" not in command["info"]:
            # update with the collected trace metadata
            trace_dict.update(self.get_metadata(i_transformer))
        # build transmitter to return and eventually transmit trace
        my_transmitter = self._get_transmitter(i_transformer, trace_dict)
        # if cloud capture then transmit configuration for server db storage
        category = command['category']
        if category == 'Capture' or category == 'Autoset':
            my_transmitter.transmit_config()

        return my_transmitter

    def record_start(self):
        try:
            instrument_type = self.setup['instrument_type']
        except:
            instrument_type = 'CopleyADP-055-18'
        instrument_state = {
            'instrument_type': instrument_type,
            'status': 'Busy',
        }
        command = {
            'id': self.setup['id'],
            'status': 'in progress',
        }
        data = {
            'command': command,
            'utilization': 'start',
            'instruments': [instrument_state],
        }
        self.update_gateway_state(state=data)


class MotorClient(CommandRunner):

    def __init__(self, *args, **kwargs):
        super(MotorClient, self).__init__(*args, **kwargs)
        self.setup = collections.defaultdict(str)
        self.last_setup = None
        # the connection to the copley card
        self.card = None
        # self.card = Motor(CLIENT_SETTINGS["CANOPEN_ADDRESS"])
        self.frames_list = []
        self.last_frame = 0
        try:
            self.card.open(baud=1000000)
            # set the heartbeat to once every 500 milliseconds
            self.card.send_sdo(address=[0x10, 0x17, 0x00], data=[0xf4, 0x01],
                               acknowledge=True)
        except ValueError as e:
            logger.error("MotorClient __init__ warning: %s" % e)
        except Exception as e:
            logger.error("MotorClient __init__ error: %s" % e)
        try:
            self.card.clear_pdos()
        # except CmdErr as e:
        #     logger.warning("CmdErr %s" % e)
        except Exception as e:
            logger.warning("clear_pdos() e: %s" % e)
        self.busy = False
        post_config_form([{
            "manufacturer": "Copley",
            "product": "ADP-055-18",
            "instrument_type": "CopleyADP-055-18"
        }])
        self.start_time = time.time()
        self.insert_index = 0
        # do frames get saved and uploaded? Turns on when the "start_frames"
        # command is received. This is separate from the canbus run.
        self.logging_frames = False

    def check_motor(self, update_command=True, status="Ready"):
        """Checks acquisition type to check if scope working"""
        start_tag = max(len(self.card.frames_list)-1, 0)
        self.card.get_nmt_states()
        flags = self.card.read_all_flags()
        for node in flags:
            if "Fault" in flags[node]["status_word"]:
                status = "Fault"
        if len(self.card.emcy_msgs) > 0:
            emc_msgs = self.card.emcy_msgs[-1]
        else:
            emc_msgs = "No emergency messages detected"

        state = {"status": status, "model": "ADP-055-18",
                 "manufacturer": "Copley",
                 "instrument_type": "CopleyADP-055-18",
                 "flags": flags, 'nmt_states': self.card.nmt_states,
                 "connection": self.card.channel,
                 'emcy_msgs': emc_msgs,
                 }
        self.update_gateway_state({'instruments': [state]})
        for i in range(start_tag, len(self.card.frames_list)):
            if len(self.card.frames_list) <= i:
                logger.error("Got impossible frames_list index, start was: %s "
                             "length was %s, i was %s"
                             % (start_tag, len(self.card.frames_list), i))
                break
            self.card.frames_list[i].health_check = True
        if update_command:
            self.update_commands(status="complete")

    def clear_latch(self):
        logger.info("clearing latch")
        self.card.send_sdo(address='latching_fault_status_register',
                           data=[0xFF, 0xFF, 0xFF, 0xFF])
        self.check_motor()

    def start_frames(self):
        self.logging_frames = True
        self.update_commands(status="complete")

    def stop_frames(self):
        self.logging_frames = False
        self.update_commands(status="complete")

    def clear_frames(self):
        self.frames_list = []
        self.last_frame = 0
        self.post_frames(self.frames_list, by_command=False)
        self.update_commands(status="complete")

    def gen_data(self):
        command_id = self.setup["id"]
        if command_id == 0:
            raise ValueError("Test run id is zero! Setup is:" + str(
                self.setup))
        return {"command_id": command_id}

    def get_frame(self, frame_index=-1):
        # two routes: either the setup came from the omniclient, in which case we already
        #  have the frames, or it came from /motor/canbus
        if self.setup["category"] == "CanBus":
            _data = self.gen_data()
            if frame_index:
                _data["frame_index"] = frame_index
            response = self.get(CANBUS_URL, headers=get_headers(),
                                params=_data)
            assert response.status_code == 200
            response = response.json()
            if response == "No data found for request":
                return None
            return response
        else:
            if frame_index:
                pass
                # return interpret_expression(self.setup["frames"][frame_index])
            else:
                # frames = [interpret_expression(frame) for frame in self.setup["frames"]]
                # new_frames = []
                # for frame in frames:
                #     if isinstance(frame, list):
                #         for sf in frame:
                #             new_frames.append(sf)
                #     else:
                #         new_frames.append(frame)
                # return {"frames": new_frames}
                return

    def post_frame(self, frame):
        _data = self.gen_data()
        _data["frames"] = [frame]
        response = self.post(CANBUS_URL, headers=get_headers(),
                             data=dumps(_data))
        assert response.status_code == 200

    def post_frames(self, output_frames=None, by_command=True):
        if by_command:
            _data = self.gen_data()
        else:
            _data = {"command_id": "latest" + COMMON_SETTINGS['HARDWARENAME']}
        _data["frames"] = output_frames
        if output_frames is None:
            _data["frames"] = self.card.frames_list
            self.last_frame = len(self.card.frames_list)
        _data["frames"] = [{'id': f.id, 'time': f.time, 'data': list(f.data),
                            'written': True, 'health_check': f.health_check}
                           for f in _data["frames"]]
        _data["time"] = str(time.time() - self.start_time)
        response = self.post(CANBUS_URL, headers=get_headers(),
                             data=dumps(_data))
        assert response.status_code == 200

    def update_frame(self, new_vals, index=-1):
        _data = self.gen_data()
        if isinstance(new_vals, list):
            _data["frames"] = []
            if len(new_vals) == 0:
                logger.warning("no frames to update!")
                return
            for frame in new_vals:
                _data["frames"].append(frame)
        else:
            _data.update(new_vals)

        if "method" not in _data.keys():
            if index == -1:
                _data["method"] = "update"
            else:
                _data["method"] = "insert"
                _data["frame_index"] = index

        _data["time"] = str(time.time() - self.start_time)
        response = self.put(CANBUS_URL, headers=get_headers(),
                            data=dumps(_data))
        assert response.status_code == 200

    def get_lsusb_id(self, tag='Kvaser'):
        devices = gateway_helpers.get_usb_devices()
        for dev in devices:
            try:
                assert tag in dev['tag']
                return dev['usb_id']
            except:
                pass

    def run(self):
        gateway_status_interval = 30
        gateway_status_counter = 0
        buffer_seconds_btw_gets = 0.5
        while True:
            self.update_activity_file()
            time.sleep(buffer_seconds_btw_gets)
            gateway_status_counter += 1
            if gateway_status_interval == gateway_status_counter:
                self.check_motor(update_command=False)
                gateway_status_counter = 0
            if self.logging_frames:
                # update the frames
                self.copy_frames()
                if self.last_frame < len(self.frames_list):
                    self.post_frames(self.frames_list, by_command=False)
            try:
                # get the command from the multiprocessing queue

                if os.path.exists(COMMAND_FILENAME):
                    fh = open(COMMAND_FILENAME, "r")
                    read_command = pickle.load(fh)
                    fh.close()
                else:
                    continue
                instrument_type = ''
                if "info" in read_command:
                    read_command.update(read_command["info"])
                if "instrument_type" in read_command:
                    instrument_type = read_command["instrument_type"]
                if instrument_type == "CopleyADP-055-18":
                    command = read_command
                else:
                    continue
                if not isinstance(command, dict):
                    logger.warning("Command: %s not a dict!" % command)
                    continue
                if 'error' in command:
                    if 'Index error:' in command['error']:
                        # just means there's no command, check again later
                        pass
                    else:
                        logger.warning("error in command: %s" % command)
                    continue
                self.setup = command
                if command["id"] == "":
                    logger.error("Id is empty in command: %s" % command)
                self.busy = True
                self.record_start()
                if self.setup["category"] == "Config":
                    self.run_motor_trace()

                if "frames" in self.setup or self.setup["category"] == "CanBus":
                    self.run_canbus()
                if self.setup["category"] == "Misc":
                    if self.setup["arg"] == 'check_health':
                        # stop canbus doesn't do anything
                        self.check_motor()
                    elif self.setup["arg"] == "clear_faults":
                        self.clear_latch()
                    elif self.setup["arg"] == 'clear_frames':
                        self.clear_frames()
                    elif self.setup["arg"] == 'start_frames':
                        self.start_frames()
                    elif self.setup["arg"] == 'stop_frames':
                        self.stop_frames()
                self.update_commands(status="complete")
                utilization.record_end()
                self.busy = False
                self.update_instrument_status(status="Ready")
            except Exception as e:
                logger.info("motor error: %s" % e)
                SENTRY_CLIENT.captureException()
                self.update_commands('failed')
                logger.warning(e)
                self.busy = False
                self.update_instrument_status(status="Ready")

    def update_instrument_status(self, status, instrument_type=''):
        if instrument_type == '':
            instrument_type = 'CopleyADP-055-18'
        instrument_state = {
            'instrument_type': instrument_type,
            'status': status
        }
        self.update_gateway_state({'instruments': [instrument_state]})

    def copy_frames(self):
        for frame in self.card.frames_list:
            self.frames_list.append(deepcopy(frame))
        self.card.frames_list = []

    def run_canbus(self):
        self.start_time = time.time()
        # get all frames
        incoming_frame = self.get_frame(frame_index=None)
        for retry_numb in range(MAX_RETRIES):
            if incoming_frame:
                break
            else:
                time.sleep(BREATH_TIME)
                incoming_frame = self.get_frame(frame_index=None)
        if not incoming_frame:
            # no frames received
            logger.error("No frames received after " + str(MAX_RETRIES) +
                         " attempts")
            self.update_commands(status="failed")
            return
        else:
            if "frames" in incoming_frame:
                frames_to_write = incoming_frame["frames"]
            else:
                frames_to_write = [incoming_frame]
        output_frames = []
        for frame_to_write in frames_to_write:
            self.copy_frames()
            if frame_to_write is None:
                continue
            if "expression" in frame_to_write:
                wait_regex = "^WAIT ([\d]+|[\d]+\.[\d]+) SECONDS$"
                if frame_to_write["expression"] == "DOWNLOAD":
                    # insert a spacer frame so that the analysis doesn't
                    # trigger the data download
                    self.card.property_getter("trace_data", use_sdo=True)
                    # overwrite the first frame
                elif frame_to_write["expression"] == "WAIT FOR TRACE":
                    self.card.wait_for_trace(software_trace=False)
                elif match(wait_regex, frame_to_write["expression"]):
                    _match = match(wait_regex, frame_to_write["expression"])
                    sleep_time = float(_match.group(1))
                    time.sleep(sleep_time)
                else:
                    raise ValueError("unsure what to do about expression: %s"
                                     % frame_to_write["expression"])

            else:
                pass
                # xmit_frame = CanFrame(id=frame_to_write["id"],
                #                       data=frame_to_write["data"])
                # output_frames.append(deepcopy(xmit_frame))
                # self.card.xmit(xmit_frame, timeout=self.card.timeout,
                #                append=False)
                # self.card.acknowledge()
            for frame in self.card.frames_list:
                output_frames.append(deepcopy(frame))
        self.post_frames(output_frames)
        self.card.frames_list = []
        for frame in output_frames:
            self.card.frames_list.append(deepcopy(frame))
        self.update_commands()

    def run_motor_trace(self):
        # Trace data mode

        logger.info("Started Motor Trace")
        self.card.clear_pdos()
        logger.info("Cleared PDOs")
        if self.card.unplugged:
            return
        test_order = self.setup
        logger.info("Motor setup is: %s pos is: %s target is: %s relative %s"
                    % (self.setup["id"],
                       self.card.property_getter("actual_position"),
                       test_order["motor_end_position"],
                       test_order["relative_move"]))
        if "node_id" in test_order:
            if isinstance(test_order["node_id"], basestring):
                node_id = int(test_order["node_id"], 16)
            else:
                node_id = test_order["node_id"]
            if not 0 <= node_id <= 16:
                logger.error("Got invalid node id: %s" % node_id)
                return
            self.card.node = node_id
        # self.card.monitor_registers = registers
        if not isinstance(test_order, dict):
            raise ValueError("Config Excerpt is invalid " + test_order)
        if "timeout" not in test_order:
            logger.warning("No trace timeout, setting to 60 seconds")
            test_order["timeout"] = 60
        if "trace_period" not in test_order:
            logger.warning("No trace period, setting to 110")
            test_order["trace_period"] = 110

        if "motor_end_position" not in test_order:
            logger.warning("No Motor end position, setting to 0")
            test_order["motor_end_position"] = 0.0

        test_order["properties"] = [str(prop) for prop in test_order["properties"]]  # noqa
        self.card.start_time = time.time()
        _dp = self.card.do_trace(destination=test_order["motor_end_position"],  # noqa
                                 trace_period=test_order["trace_period"],
                                 properties=test_order["properties"],
                                 relative=test_order["relative_move"],
                                 trace_timeout=test_order["timeout"])
        # update the test to complete, then return to idle
        _data = self.gen_data()
        _data["channels"] = _dp

        if len(self.card.flag_timestamps) > 0:
            measurements = []
            for timestamp in self.card.flag_timestamps:
                display_name = timestamp[1]
                display_name += " appears" if timestamp[2] else " disappears"
                measurements.append({
                    "value": timestamp[0],
                    "display_name": display_name,
                    "ivi_name": display_name.replace(" ", "_"),
                    "units": "seconds",
                    "type": "status_flag",
                })
            measurements = {"no_channel": measurements}
        else:
            # if self.card.monitor_registers:
            #     logger.warning("The monitor registers were set to: " +
            #                    str(self.card.monitor_registers) +
            #                    " but no flags were detected!")
            measurements = None
        transmitter = CANOpenTransmitter(data=_data, config=self.setup,
                                         measurements=measurements)
        tgt_reached = self.card.trace_target_reached
        transmitter.results_dict["target_reached"] = tgt_reached
        transmitter.transmit_trace()
        self.setup["result_id"] = transmitter.results_dict['results_id']
        logger.info("Done motor trace")
        return

    def update_canbus_response(self, frame_to_write=None):
        # overwrite the first frame
        if frame_to_write is not None:
            if not isinstance(frame_to_write, dict):
                frame_to_write = frame_to_write
            if "frame_index" not in frame_to_write.keys():
                frame_to_write["frame_index"] = self.insert_index
            frame_to_write["written"] = True
            self.update_frame(frame_to_write)
            self.insert_index += 1
        if len(self.card.frames_list) > 0:
            self.update_frame(self.card.frames_list, index=self.insert_index)
            self.insert_index += len(self.card.frames_list)
