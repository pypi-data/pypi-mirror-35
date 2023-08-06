# -*- coding: utf-8 -*-

import sys
import locale
import platform

from miko.logger import logger

# Global name
__version__ = '0.1.dev09021825'
__author__ = 'ysicing zheng <i@spanda.io>'
__license__ = 'AGPLv3'


try:
    from psutil import __version__ as psutil_version
except ImportError:
    print("Not found psutil library. Miko cannot start.")
    print("You can: pip install psutil")
    sys.exit(1)

try:
    locale.setlocale(locale.LC_ALL, '')
except locale.Error:
    print("Warning: Unable to set locale. Expect encoding problems.")

if sys.version_info < (2, 7) or (3, 0) <= sys.version_info < (3, 4):
    print("Miko requires at least Python 2.7 or 3.4 to run.")
    sys.exit(1)

psutil_min_version = (5, 3, 0)
psutil_version_info = tuple([int(num) for num in psutil_version.split('.')])
if psutil_version_info < psutil_min_version:
    print("psutil 5.3.0 or higher is needed. Miko cannot start.")
    print("You can: pip install -U psutil")
    sys.exit(1)


def main():
    """Main entrypoint for miko

    :return:
    """

    logger.info('Start Miko {}'.format(__version__))
    logger.info('{} {} and psutil {} detected'.format(
        platform.python_implementation(),
        platform.python_version(),
        psutil_version
    ))

    print("Hello Miko...")
