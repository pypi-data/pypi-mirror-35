#!/usr/bin/env python
#coding:utf-8

from __future__ import unicode_literals

import os
import os.path
import sys
import re
import argparse

__version__ = "1.0.1"

def main():
    parser          = argparse.ArgumentParser(
    prog            = u'yos',
    version         = __version__,
    description     = u'yos tools',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(u'-l', u'--list', action=u'store_true', default = False, help=u'list all commands.')
    ns = parser.parse_args(sys.argv[1:])
    print ns

if __name__ == '__main__':
    main()

