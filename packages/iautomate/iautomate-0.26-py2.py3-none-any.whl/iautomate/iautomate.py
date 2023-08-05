import json
import os
from collections import OrderedDict
from . import global_variables
from .resources import abstract_resource
from .resources import execution_resource
from .resources import file_resource
from .resources import package_resource
from .resources import service_resource
from .resources import directory_resource


class IAutomate(object):
    VARS_KEY = 'vars'
    TASKS_KEY = 'tasks'

    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.__parse_config_file()
        self.global_variables = self.config.get(self.VARS_KEY, None)

    @property
    def config_file(self):
        return self.__config_file

    @config_file.setter
    def config_file(self, config_file):
        # check if the config file exists
        if os.path.isfile(config_file) is True:
            self.__config_file = config_file
        else:
            raise OSError('Config file does not exist: ' + config_file)

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, config):
        # check if the config file is not empty
        if config:
            self.__config = config
        else:
            raise OSError('Config cannot be empty')

    @property
    def global_variables(self):
        return self.__global_variables

    @global_variables.setter
    def global_variables(self, variables):
        # check if the config file is not empty
        self.__global_variables = global_variables.GlobalVariables(variables)

    # parse the config file which is in json
    def __parse_config_file(self):
        return json.load(open(self.config_file), object_pairs_hook=OrderedDict)

    # handle execution resource
    def __handle_execs(self, execs):
        for execution in execs:
            self.__handle_exec(execution)

    # handle execution resource
    def __handle_exec(self, execution_properties):
        # instantiate execution model and run it
        execution = execution_resource.ExecutionResource(execution_properties, self.global_variables)
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
        package = package_resource.PackageResource(package_properties, self.global_variables)
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
        service = service_resource.ServiceResource(service_properties, self.global_variables)
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
        file_resource_obj = file_resource.FileResource(file_properties, self.global_variables)
        file_resource_obj.run()

        if file_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY, None):
            self.__handle_tasks(file_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY))

    # handle directory resources
    def __handle_directories(self, directories):
        # iterate through the directories
        for directory in directories:
            self.__handle_directory(directory)

    def __handle_directory(self, directory_properties):
        # instantiate directory model and run it
        directory = directory_resource.DirectoryResource(directory_properties, self.global_variables)
        directory.run()

        if directory_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY, None):
            self.__handle_tasks(directory_properties.get(abstract_resource.AbstractResource.AFTER_TASKS_KEY))

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
            elif config_type == 'directories':
                print('| Handling directories ...')
                self.__handle_directories(properties)
            else:
                # unsupported resource
                print('Unsupported resource: ' + config_type)

    # run the tasks in the config file
    def run(self):
        print('Processing the config file ...')
        self.__handle_tasks(self.config[self.TASKS_KEY])
