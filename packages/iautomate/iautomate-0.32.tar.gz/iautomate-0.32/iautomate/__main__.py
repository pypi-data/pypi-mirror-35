import sys
from iautomate import IAutomate
import traceback
import os


def main():
    # check running as sudo:
    if not os.geteuid() == 0:
        sys.exit("\nYou must run this script as sudo\n")

    # check config file is provided
    try:
        config_file = sys.argv[1]
    except IndexError:
        print('Error: Config file is missing')
        return

    try:
        iautomate = IAutomate(config_file)
        iautomate.run()
    except Exception as e:
        print('Error: ' + str(e))


if __name__ == '__main__':
    sys.exit(main())
