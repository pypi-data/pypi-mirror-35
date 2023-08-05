class GlobalVariables(object):
    DOC_ROOT_KEY = 'doc_root'
    DEBUG_KEY = 'debug'
    SUDO_KEY = 'sudo'

    def __init__(self, variables):
        self.sudo = variables.get(self.SUDO_KEY, None)
        self.debug = variables.get(self.DEBUG_KEY, None)
        self.doc_root = variables.get(self.DOC_ROOT_KEY, None)

    @property
    def sudo(self):
        return self.__sudo

    @sudo.setter
    def sudo(self, sudo):
        self.__sudo = sudo

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, debug):
        self.__debug = debug

    @property
    def doc_root(self):
        return self.__doc_root

    @doc_root.setter
    def doc_root(self, doc_root):
        self.__doc_root = doc_root

    # is in debug mode
    def is_debug_mode(self):
        return True if self.debug else False

    # is sudo is enabled
    def is_sudo_enabled(self):
        return True if self.sudo else False
