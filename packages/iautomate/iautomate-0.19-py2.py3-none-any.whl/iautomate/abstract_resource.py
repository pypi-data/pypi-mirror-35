from abc import ABCMeta, abstractmethod

import shell_helper


class AbstractResource(object):
    __metaclass__ = ABCMeta

    AFTER_TASKS_KEY = 'after_tasks'

    @abstractmethod
    def __init__(self, properties, global_variables=None):
        self.properties = properties
        self.global_variables = global_variables
        self.name = properties['name']
        self.action = properties.get('action', None)
        self.sudo = properties.get('sudo', None)

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties):
        self.__properties = properties

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action):
        self.__action = action

    @property
    def sudo(self):
        return self.__sudo

    @sudo.setter
    def sudo(self, sudo):
        self.__sudo = sudo

    @property
    def global_variables(self):
        return self.__global_variables

    @global_variables.setter
    def global_variables(self, global_variables):
        self.__global_variables = global_variables

    @abstractmethod
    def run(self):
        pass

    # check if sudo is enabled
    def is_sudo_enabled(self):
        # if self.sudo exists, it overwrites the global variable
        if self.sudo is True or self.sudo is False:
            return self.sudo

        if self.global_variables and 'sudo' in self.global_variables and self.global_variables['sudo'] is True:
            return True
        else:
            return False

    # run the shell command and print the output if is in debug mode
    def _run_shell_command(self, command):
        # determine sudo
        sudo = 'sudo ' if self.is_sudo_enabled() is True else ''

        output = shell_helper.ShellHelper.run_command(sudo + command)
        if self.is_debug_mode() is True:
            print('* Running: ' + command)
            print('** Output: ')
            print(output)

        # make sure there is no whitespace in the output
        return output.strip()

    # is in debug mode
    def is_debug_mode(self):
        if self.global_variables and 'debug' in self.global_variables and self.global_variables['debug'] is True:
            return True
        else:
            return False
