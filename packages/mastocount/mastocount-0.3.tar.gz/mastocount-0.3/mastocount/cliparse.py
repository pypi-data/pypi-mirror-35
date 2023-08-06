# -*- coding: utf-8 -*-
# Copyright © 2017-2018 Carl Chenet <carl.chenet@ohmytux.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# CLI parsing
'''CLI parsing'''

# standard library imports
from argparse import ArgumentParser
import glob
import logging
import os.path
import sys

__version__ = '0.3'

def cliparse():
    '''Parse the command line to get options'''
    epilog = 'For more information: https://mastocount.readhthedocs.org'
    description = 'Count Mastodon followers of different accounts (details and total sum)'
    parser = ArgumentParser(prog='mastocount',
                            description=description,
                            epilog=epilog)
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-c', '--config',
                        default=[os.path.join(os.getenv('XDG_CONFIG_HOME', '~/.config'),
                                              'mastocount.ini')],
                        nargs='+',
                        dest="config",
                        help='Location of config file (default: %(default)s)',
                        metavar='FILE')
    opts = parser.parse_args()
    # verify if the path to cache file is an absolute path
    # get the different config files, from a directory or from a *.ini style
    opts.config = list(map(os.path.expanduser, opts.config))
    opts.configs = []
    for element in opts.config:
        if element and not os.path.exists(element):
            sys.exit('The file does not exist: {filepath}'.format(filepath=element))
        if os.path.isdir(element):
            for i in glob.glob(os.path.join(element, '*.ini')):
                opts.configs.append(i)
        else:
            # trying to glob the path
            for i in glob.glob(element):
                opts.configs.append(i)
    # verify if a configuration file is provided
    if not opts.configs:
        sys.exit('no configuration file was found at the specified path(s) with the option -c')
    return opts
