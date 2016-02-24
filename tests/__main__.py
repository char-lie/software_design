from sys import exit
from argparse import ArgumentParser
from cProfile import Profile
from pstats import Stats
from unittest import TestSuite, TextTestRunner

from tests import tests


if __name__ == '__main__':
    exit_status = not TextTestRunner().run(TestSuite(tests)).wasSuccessful()
    exit(exit_status)

