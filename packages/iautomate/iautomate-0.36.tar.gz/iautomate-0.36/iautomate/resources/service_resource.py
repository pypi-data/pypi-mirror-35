from . import abstract_resource


class ServiceResource(abstract_resource.AbstractResource):
    def __init__(self, properties, global_variables=None):
        super(ServiceResource, self).__init__(properties, global_variables)
        self.ensure = properties.get('ensure', None)

    @property
    def ensure(self):
        return self.__ensure

    @ensure.setter
    def ensure(self, ensure):
        self.__ensure = ensure

    # compare the service status with the given status
    def is_current_status_right(self):
        if self.ensure == 'restarted':
            status = 'running'
        else:
            status = self.ensure

        return True if self.current_status() == status else False

    # check a service status e.g. running, dead
    def current_status(self):
        # get service status
        status = self._run_shell_command('service ' + self.name + ' status')

        if 'is running' in status:
            return 'running'
        else:
            return 'dead'

    def run(self):
        if self.is_current_status_right() is False:
            # given status does not match with the current status of the service
            if self.ensure == 'running':
                # try to start the service
                self._run_shell_command('service ' + self.name + ' start')
            elif self.ensure == 'dead':
                # try to stop the service
                self._run_shell_command('service ' + self.name + ' stop')
            elif self.ensure == 'restarted':
                # try to restart the service
                self._run_shell_command('service ' + self.name + ' restart')

            # check the status again
            if self.is_current_status_right() is False:
                # service status is still the same cannot do much about it
                raise Exception('was not able to change the service status to ' + self.ensure)

        print('*' + self.name + '* is ' + self.ensure)
