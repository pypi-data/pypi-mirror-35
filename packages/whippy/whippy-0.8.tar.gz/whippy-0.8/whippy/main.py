import sys
import getopt
from classes.WPPy import WPPy


def main(argv):
    use_defaults = False

    try:
        opts, args = getopt.getopt(argv, "d", ["defaults"])
    except getopt.GetoptError:
        print('whippy [-d|--defaults]')
        sys.exit()

    for opt, arg in opts:
        if opt == "-d" or opt == "--defaults":
            use_defaults = True

    wppy = WPPy(use_defaults)
    wppy.create_wp_database()
    wppy.create_wp_site()
