from ..helpers import string_helper
from . import abstract_resource
import os


class DirectoryResource(abstract_resource.AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(DirectoryResource, self).__init__(properties, global_variables)
        self.owner = properties.get('owner', None)
        self.group = properties.get('group', None)
        self.mode = properties.get('mode', None)
        self.ensure = properties.get('ensure', None)

    # overwrite the parent get
    @property
    def name(self):
        # update the name if doc_root is presented in it
        if self.global_variables and self.global_variables.doc_root:
            return string_helper.StringHelper.replace_placeholder(self.__name, '{$doc_root}',
                                                                  self.global_variables.doc_root)
        else:
            return self.__name

    # overwrite this one too, because the getter is already overwritten
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        self.__group = group

    @property
    def mode(self):
        return str(self.__mode)

    @mode.setter
    def mode(self, mode):
        self.__mode = mode

    @property
    def ensure(self):
        return self.__ensure

    @ensure.setter
    def ensure(self, ensure):
        self.__ensure = ensure

    def run(self):
        if self.action == 'create':
            # check if directory does not exist
            if os.path.isdir(self.name) is not False:
                raise OSError('Cannot create the dir: ' + self.name + ' It already exists')

            # directory does not exist, create it
            self._run_shell_command('mkdir ' + self.name)

            # check if the directory has been created
            if os.path.isdir(self.name) is not True:
                raise OSError('Unable to create the dir: ' + self.name)

            # set owner and group
            self._run_shell_command('chown ' + self.owner + ':' + self.group + ' ' + self.name)

            # set mode
            self._run_shell_command('chmod ' + self.mode + ' ' + self.name)
        elif self.action == 'remove' and os.path.isdir(self.name) is True:
            self._run_shell_command('rm -rf ' + self.name)

            # check if the folder has been removed
            if os.path.isdir(self.name) is not False:
                raise OSError('Unable to delete directory: ' + self.name)

        # for the time being check 'present' after action
        if self.ensure == 'present' and os.path.isdir(self.name) is not True:
            raise OSError('Folder: ' + self.name + ' does not exist')
