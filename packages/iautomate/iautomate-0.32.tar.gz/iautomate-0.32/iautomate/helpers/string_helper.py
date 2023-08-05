class StringHelper(object):
    # run the shell command and print the output if is in debug mode
    @staticmethod
    def replace_placeholder(to_change_string, placeholder, value):
        return to_change_string.replace(placeholder, value)
