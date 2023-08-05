"""

Copyright (C) 2016-2017 GradientOne Inc. - All Rights Reserved
Unauthorized copying or distribution of this file is strictly prohibited
without the express permission of GradientOne Inc.

"""

import collections
import datetime
import pickle

import gateway_helpers as helpers
import json
import os
import time
import urllib
from configparser import ConfigParser
from subprocess import Popen, PIPE
from multiprocessing import Queue
from controllers import ClientInfo, BaseController
from command_runners import MotorClient
from base import BaseClient
from os.path import exists
from scope import ScopeClient


# Read in config file info
cfg = ConfigParser()
PATH_TO_CFG_FILE = '/etc/gradient_one.cfg'
cfg.read(PATH_TO_CFG_FILE)
COMMON_SETTINGS = cfg['common']
CLIENT_SETTINGS = cfg['client']

# Get Sentry client for logging
SENTRY_CLIENT = helpers.get_sentry()


# Set globals
SECONDS_BTW_HEALTH_UPDATES = 30
CMD_URL = helpers.BASE_URL + '/instructions.json'
DIRPATH = os.path.dirname(os.path.realpath(__file__))
if COMMON_SETTINGS['DOMAIN'].find("localhost") == 0 or COMMON_SETTINGS['DOMAIN'].find("127.0.0.1") == 0:  # noqa
    BASE_URL = "http://" + COMMON_SETTINGS['DOMAIN']
else:
    BASE_URL = "https://" + COMMON_SETTINGS['DOMAIN']
logger = helpers.logger

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"


def scope_client(client_info):
    """Starts the manager for getting and running configs"""
    logger.info("initializing ScopeClient in scope_client")
    client = ScopeClient(client_info=client_info)
    client.run()


def motor_client(client_info):
    """Starts the manager for getting and running configs"""
    pid_file = os.path.join(DIRPATH, 'motor_client.pid')
    with open(pid_file, 'w') as f:
        f.write(str(os.getpid()))
    client = MotorClient(client_info=client_info)
    client.run()


class HealthClient(BaseClient):

    def __init__(self, *args, **kwargs):
        super(HealthClient, self).__init__(*args, **kwargs)

    """Manages process that posts gateway health info"""

    def put_health_data(self):
        """makes PUT with the health data to server"""
        url = helpers.BASE_URL + '/gateway/health'
        instruments = helpers.get_known_connected_instruments()
        payload = {
            "name": COMMON_SETTINGS['HARDWARENAME'],
            "company": COMMON_SETTINGS['COMPANYNAME'],
            "client_version": self.get_client_version(),
            "instruments": instruments,
            "status": "Online",
            "message": "No events"
        }
        logger.info("Updating gateway health state with %s" % payload)
        self.put(url, data=json.dumps(payload))
        url = helpers.BASE_URL + '/discovered_devices'
        payload = {
            'discovered devices': instruments,
        }
        self.post(url, data=json.dumps(payload))

    def run(self, client_info):
        """Runs the health manager indefinitely"""
        while True:
            logger.info("HealthClient is alive")
            try:
                self.put_health_data()
                self.post_logfile()
                self.update_activity_file(client_info.activity_file)
            except Exception:
                logger.info("post health data exception", exc_info=True)
                SENTRY_CLIENT.captureException()
            time.sleep(SECONDS_BTW_HEALTH_UPDATES)

    def get_client_version(self, package='gradientone'):
        """Gets version by parsing pip output"""
        version = {}
        try:
            version_file = os.path.join(DIRPATH, 'version.py')
            with open(version_file) as f:
                exec(f.read(), version)
            version = version['__version__']
        except Exception as e:
            logger.warning("Unable to read version file %s" % e)
        if not version:
            version = ""
            try:
                pip_show_pkg = ['pip', 'show', package]
                output = Popen(pip_show_pkg, stdout=PIPE).communicate()[0]
                lines = output.split('\n')
                for line in lines:
                    if line.startswith("Version:"):
                        version = line.split(':')[1].strip()
            except Exception as e:
                logger.warning("Unable to read pip version %s" % e)
        return version


def health_updates(client_info):
    """Runs the manager that posts gateway health info"""
    pid_file = os.path.join(DIRPATH, 'health_updates.pid')
    with open(pid_file, 'w') as f:
        f.write(str(os.getpid()))
    client = HealthClient()
    client.run(client_info)


def special_commands(client_info):
    pid_file = os.path.join(DIRPATH, 'special_commands.pid')
    with open(pid_file, 'w') as f:
        f.write(str(os.getpid()))
    client = SpecialCommandsClient()
    client.run(client_info)


class SpecialCommandsClient(BaseClient):

    def __init__(self, *args, **kwargs):
        super(SpecialCommandsClient, self).__init__(*args, **kwargs)

    def run(self, client_info):
        while True:
            time.sleep(1)
            try:
                # check the command queue for new commands
                command = self.client_info.command_queue.get()
            except:
                continue
            try:
                self.process_command(command)
                self.update_activity_file(client_info.activity_file)
            except Exception as e:
                logger.error("Unexpected exception %s" % e, exc_info=True)

    def process_response(self, response):
        command = response.json()['commands'][0]
        logger.info("Processing Special Command: %s" % command)
        self.process_command(command)

    def process_command(self, command):
        cat = command['category']
        if cat == 'UpdateConfigFile':
            if command['arg']:
                self.update_cfg(command)
            else:
                logger.warning("Unexpected arg %s" % command['arg'])
        else:
            logger.warning("Unexpected command category %s" % cat)

    def update_cfg(self, command):
        """Grabs the new config file from the server"""
        cfgfile = urllib.URLopener()
        cfgfile.retrieve(command.arg, PATH_TO_CFG_FILE)


class GatewayClient(BaseController):

    def __init__(self, *args, **kwargs):
        name = 'gateway_client'
        super(GatewayClient, self).__init__(name=name, *args, **kwargs)

        """Gathers the client infos to run with controller

        The targets and names are used to create ClientInfo objects used in
        the BaseController run() method. The keep_alive_interval
        is the seconds allowed to pass between updates to the activity file
        before the controller will restart the client process.

        Note that the BaseController will pass the ClientInfo object
        to the target function so that the function will have the client
        info, most importantly the activity_file that it needs to update
        periodically within the keep_alive_interval

        clients_dict - a dictionary with a k,v pair for each client this
            controller is in charge of. That k,v pair will have the
            client name for the key and the a ClientInfo object value
        """

        hposts_info = ClientInfo(
            target=health_updates,
            name='health_updates',
            keep_alive_interval=120,
        )

        self.scope_command_queue = Queue()
        scope_info = ClientInfo(
            target=scope_client,
            name='scope_client',
            keep_alive_interval=1200,
            command_queue=self.scope_command_queue,
        )
        # self.motor_command_queue = Queue()
        # motor_info = ClientInfo(
        #     target=motor_client,
        #     name='motor_client',
        #     keep_alive_interval=120,
        #     command_queue=self.motor_command_queue,
        # )
        self.special_command_queue = Queue()
        spec_info = ClientInfo(
            target=special_commands,
            name='special_commands',
            keep_alive_interval=120,
            command_queue=self.special_command_queue,
        )
        client_infos = [scope_info, hposts_info, motor_info, spec_info]
        self.instruction_id = None

        # Other clients to be run by the GatewayClient should
        # be added here. Be sure to create a ClientInfo object with
        # the appropriate target, name, keep_alive_interval, and
        # activity file. Then append the ClientInfo to client_infos

        # These client_info's will specify the client processes to be started
        # when the GatewayClient method run_clients() is called
        self.clients_dict = collections.defaultdict(str)
        for client_info in client_infos:
            self.clients_dict[client_info.name] = client_info

        # the number of seconds between each check in for seeing if
        # sub clients are still running
        self.keep_alive_check_inteval = 5

    def _check_for_instructions(self):
        second_counter = 0
        while True:
            self.get_and_handle_instructions()
            if second_counter == self.keep_alive_check_inteval:
                # check in with each client
                self.keep_clients_alive()
                second_counter = 0

            time.sleep(1)
            second_counter += 1

    def run_clients(self):
        """Starts the clients and keeps them alive

        First iterates through the ClientInfo objects in the
        clients_dict attribute and starts each client process according
        to the info in the that client's ClientInfo object.

        Then this function runs a loop every 5 seconds that checks the
        activity files of each client process to make sure those
        clients are still updating. If the time (seconds) since the
        last update to a given client's activity file was longer than
        that client's keep_alive_interval then the client process is
        restarted. As part of the restart, the client's activity file
        is updated with the current loop's time (c_time).
        """
        # start up each client
        for name in self.clients_dict:
            logger.info("run_clients() STARTING CLIENT %s" % name)
            client_info = self.clients_dict[name]
            self.start_process(client_info.target, name=client_info.name,
                               ps_args=(client_info,))
        # begin running the main loop for the gateway client
        self.run()

    def keep_clients_alive(self):
        """Checks in with each client to keep alive

        If a client process has not checked in with the
        activity file within it's keep alive interval, then
        the client process is restarted
        """
        for name in self.clients_dict:
            client = self.clients_dict[name]
            c_time = datetime.datetime.now()
            fmt = DATETIME_FORMAT
            act_time_str = self.read(client.activity_file)
            try:
                act_time = datetime.datetime.strptime(act_time_str, fmt)
            except Exception as e:
                logger.warning("Activity time exception: %s" % e)
                act_time = c_time
            delta = c_time - act_time
            if delta.total_seconds() > client.keep_alive_interval:
                logger.warning("%s exceeded keep alive interval" % name)
                self.restart_process(target=client.target, name=name,
                                     ps_args=(client,))
                logger.info("restarting process for %s" % name)
                self.write(client.activity_file, c_time.strftime(fmt))


###################################################################

# Start of sample code, not part of normal gateway client operation

###################################################################


def simple_client_a(client_info):
    while True:
        logger.info("Simple client A checking command q:")
        try:
            command = client_info.command_queue.get(block=False)
        except:
            command = None
        if command:
            logger.info("Simple client A command:")
            logger.info(command)
        time.sleep(1)


def simple_client_b(client_info):
    while True:
        logger.info("Simple client B checking command q:")
        try:
            command = client_info.command_queue.get(block=False)
        except:
            command = None
        if command:
            logger.info("Simple client B command:")
            logger.info(command)
        time.sleep(1)


class SimpleExample(BaseController):

    def __init__(self, *args, **kwargs):
        name = 'simple example'
        super(SimpleExample, self).__init__(name=name, *args, **kwargs)
        self.command_queue_a = Queue()
        info_a = ClientInfo(
            target=simple_client_a,
            name='simple_client_a',
            keep_alive_interval=1200,
            command_queue=self.command_queue_a,
        )
        self.command_queue_b = Queue()
        info_b = ClientInfo(
            target=simple_client_b,
            name='simple_client_b',
            keep_alive_interval=120,
            command_queue=self.command_queue_b,
        )
        client_infos = [info_a, info_b]
        # Other clients to be run by the BaseController should
        # be added here. Be sure to create a ClientInfo object with
        # the appropriate target, name, keep_alive_interval, and
        # activity file. Then append the object to client_infos

        # These client_info's will specify the client processes to be started
        # when the BaseController method run_clients() is called
        for client_info in client_infos:
            self.clients_dict[client_info.name] = client_info

    def run_clients(self):
        """the main run method of GatewayClient"""
        self.command_queue_a.put({'number': 1})
        time.sleep(1)
        self.command_queue_b.put({'number': 1})
        time.sleep(1)
        self.command_queue_a.put({'number': 2})
        time.sleep(1)
        self.command_queue_a.put({'number': 3})
        time.sleep(1)
        self.command_queue_b.put({'number': 2})
        time.sleep(1)
        self.command_queue_b.put({'number': 3})
        super(GatewayClient, self).run_clients()

    def get_and_handle_instructions(self, *args, **kwargs):
        """don't do anything with instructions in simple example"""
        pass


if __name__ == "__main__":
    #example = SimpleExample()
    example = GatewayClient()
    example.run_clients()
