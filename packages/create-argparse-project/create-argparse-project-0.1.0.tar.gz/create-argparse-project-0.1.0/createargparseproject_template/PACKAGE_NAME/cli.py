import argparse
from .__init__ import __version__


def show_header():
    print('PROJECT_NAME v{}'.format(__version__))


def main():
    show_header()
    print('Hello world!')


if __name__ == '__main__':
    main()
