from sys import exit
import logging
from argparse import ArgumentParser
from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats
from unittest import TestSuite, TextTestRunner

from tests import tests


if __name__ == '__main__':
    parser = ArgumentParser(description='Rectangle tracker example')
    logger_levels = [logging.getLevelName(i*10) for i in xrange(6)]
    parser.add_argument('-l', '--log', help='set logger level', type=str.upper,
                                       default='ERROR', choices=logger_levels)
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.log))
    exit_status = not TextTestRunner().run(TestSuite(tests)).wasSuccessful()
    exit(exit_status)

