import sys
from iautomate import IAutomate
import traceback


def main():
    # check config file is provided
    try:
        config_file = sys.argv[1]
    except IndexError:
        print('Error: Config file is missing')
        return

    try:
        iautomate = IAutomate(config_file)
        iautomate.run()
    except Exception, e:
        print('Error: ' + e.message)
        print(traceback.format_exc())


if __name__ == '__main__':
    sys.exit(main())
