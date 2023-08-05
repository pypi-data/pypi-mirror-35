import abstract_resource
import string_helper
import os


class FileResource(abstract_resource.AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(FileResource, self).__init__(properties, global_variables)
        self.owner = properties.get('owner', None)
        self.group = properties.get('group', None)
        self.mode = properties.get('mode', None)
        self.source = properties.get('source', None)

    # overwrite the parent get
    @property
    def name(self):
        # update the name if doc_root is presented in it
        original_name = self.__name

        if self.global_variables and 'doc_root' in self.global_variables:
            return string_helper.StringHelper.replace_placeholder(original_name, '{$doc_root}', self.global_variables['doc_root'])
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, source):
        self.__source = source

    def run(self):
        if self.action == 'create':
            # check if the source file exists
            if os.path.isfile(self.source) is not True:
                raise IOError('Source file does not exist: ' + self.source)

            # check the destination
            # TODO

            # copy the source to destination
            self._run_shell_command('cp ' + self.source + ' ' + self.name)

            # check if the file has been copied
            if os.path.isfile(self.name) is not True:
                raise IOError('Could not create the file: ' + self.name)

            # set owner and group
            self._run_shell_command('chown ' + self.owner + ':' + self.group + ' ' + self.name)

            # set mode
            self._run_shell_command('chmod ' + self.mode + ' ' + self.name)
        elif self.action == 'remove':
            # check if the source file exists
            if os.path.isfile(self.name) is True:
                self._run_shell_command('rm ' + self.name)

                # check if the file has been removed
