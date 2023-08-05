import json
import os
from collections import OrderedDict

from resources.service import Service
from resources.package import Package
from resources.execution import Execution


class IAutomate(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.__parse_config_file()

    @property
    def config_file(self):
        return self.__config_file

    @config_file.setter
    def config_file(self, config_file):
        # check if the config file exists
        if os.path.isfile(config_file) is True:
            self.__config_file = config_file
        else:
            raise IOError('Config file does not exist: ' + config_file)

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, config):
        # check if the config file is not empty
        if config:
            self.__config = config
        else:
            raise IOError('Config cannot be empty')

    # parse the config file which is in json
    def __parse_config_file(self):
        return json.load(open(self.config_file), object_pairs_hook=OrderedDict)

    # is in debug mode
    def is_debug_mode(self):
        if 'vars' in self.config and 'debug' in self.config['vars'] and self.config['vars']['debug'] is True:
            return True
        else:
            return False

    # check the global variable and resource specific sudo for sudo
    def is_sudo_enabled(self, resource_sudo=None):
        # if resource_sudo exists, it overwrites the global variable
        if resource_sudo is True or resource_sudo is False:
            return resource_sudo

        if 'vars' in self.config and 'sudo' in self.config['vars'] and self.config['vars']['sudo'] is True:
            return True
        else:
            return False

    # handle executions
    def __handle_execs(self, execs):
        for execution in execs:
            self.__handle_exec(execution)

    # handle execution
    def __handle_exec(self, execution):
        # instantiate execution model and run it
        execution = Execution(execution, self.config.get('vars', None))
        execution.run()

    # handle packages
    def __handle_packages(self, packages):
        for package in packages:
            self.__handle_package(package)

    # handle package
    def __handle_package(self, package):
        # instantiate package model and run it
        package = Package(package, self.config.get('vars', None))
        package.run()

    # handle services
    def __handle_services(self, services):
        for service in services:
            self.__handle_service(service)

    # handle service
    def __handle_service(self, service):
        # instantiate service model and run it
        service = Service(service, self.config.get('vars', None))
        service.run()

    def __handle_tasks(self, tasks):
        # iterate through the task
        for task in tasks:
            self.__handle_task(task)

    def __handle_task(self, task):
        # for each task handle the sub items based on the type
        for config_type, properties in task.items():
            if config_type == 'execs':
                print('| Handling execs ...')
                self.__handle_execs(properties)
            elif config_type == 'packages':
                print('| Handling packages ...')
                self.__handle_packages(properties)
            elif config_type == 'services':
                print('| Handling services ...')
                self.__handle_services(properties)
            else:
                # unsupported resource
                print('Unsupported resource: ' + config_type)

    # run the tasks in the config file
    def run(self):
        print('Processing the config file ...')
        self.__handle_tasks(self.config['tasks'])
