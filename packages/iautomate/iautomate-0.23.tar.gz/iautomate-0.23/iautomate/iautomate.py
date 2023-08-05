import json
import os
from collections import OrderedDict

import abstract_resource
import execution_resource
import file_resource
import package_resource
import service_resource


class IAutomate(object):
    VARS_KEY = 'vars'
    DEBUG_KEY = 'debug'
    SUDO_KEY = 'sudo'
    TASKS_KEY = 'tasks'

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
        if self.VARS_KEY in self.config and self.DEBUG_KEY in self.config[self.VARS_KEY] and self.config[self.VARS_KEY][self.DEBUG_KEY] is True:
            return True
        else:
            return False

    # check the global variable and resource specific sudo for sudo
    def is_sudo_enabled(self, resource_sudo=None):
        # if resource_sudo exists, it overwrites the global variable
        if resource_sudo is True or resource_sudo is False:
            return resource_sudo

        if self.VARS_KEY in self.config and self.SUDO_KEY in self.config[self.VARS_KEY] and self.config[self.VARS_KEY][self.SUDO_KEY] is True:
            return True
        else:
            return False

    # handle execution resource
    def __handle_execs(self, execs):
        for execution in execs:
            self.__handle_exec(execution)

    # handle execution resource
    def __handle_exec(self, execution_properties):
        # instantiate execution model and run it
        execution = execution_resource.ExecutionResource(execution_properties, self.config.get(self.VARS_KEY, None))
        execution.run()

        if execution_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY, None):
            self.__handle_tasks(execution_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY))

    # handle package resource
    def __handle_packages(self, packages):
        for package in packages:
            self.__handle_package(package)

    # handle package resource
    def __handle_package(self, package_properties):
        # instantiate package model and run it
        package = package_resource.PackageResource(package_properties, self.config.get(self.VARS_KEY, None))
        package.run()

        if package_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY, None):
            self.__handle_tasks(package_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY))

    # handle service resource
    def __handle_services(self, services):
        for service in services:
            self.__handle_service(service)

    # handle service resource
    def __handle_service(self, service_properties):
        # instantiate service model and run it
        service = service_resource.ServiceResource(service_properties, self.config.get(self.VARS_KEY, None))
        service.run()

        if service_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY, None):
            self.__handle_tasks(service_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY))

    # handle file resources
    def __handle_files(self, files):
        # iterate through the files
        for file in files:
            self.__handle_file(file)

    # handle file resource
    def __handle_file(self, file_properties):
        # instantiate file model and run it
        file_resource_obj = file_resource.FileResource(file_properties, self.config.get(self.VARS_KEY, None))
        file_resource_obj.run()

        if file_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY, None):
            self.__handle_tasks(file_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY))

    def __handle_tasks(self, tasks):
        # iterate through the tasks
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
            elif config_type == 'files':
                print('| Handling files ...')
                self.__handle_files(properties)
            else:
                # unsupported resource
                print('Unsupported resource: ' + config_type)

    # run the tasks in the config file
    def run(self):
        print('Processing the config file ...')
        self.__handle_tasks(self.config[self.TASKS_KEY])
