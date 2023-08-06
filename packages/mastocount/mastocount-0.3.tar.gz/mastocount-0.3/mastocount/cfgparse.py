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
# along with this program.  If not, see <http://www.gnu.org/licenses/

# Get values of the configuration file
'''Get values of the configuration file'''

# standard library imports
from configparser import SafeConfigParser, NoOptionError, NoSectionError
import logging
import os
import os.path
import socket
import sys

# 3rd party library imports
import feedparser

# local imports
from mastocount.cfgparsers.elasticsearch import parse_elasticsearch

def cfgparse(clioptions):
    '''Parse the configurations'''
    cfgs = []
    is_elasticsearch_defined = False
    for pathtoconfig in clioptions.configs:
        options = {}
        addressflag = '@'
        # read the configuration file
        config = SafeConfigParser()
        if not config.read(os.path.expanduser(pathtoconfig)):
            sys.exit('Could not read the configuration file')
        cfg = {}
        for section in config:
            if section != 'DEFAULT':
                cfg[section] = {}
                # sections of the configuration dedicated to different accounts
                if addressflag in section:
                    # iterate in a mastodon section
                    # get user_credentials and client_credentials
                    for option in ('user_credentials', 'client_credentials'):
                        if config.has_option(section, option): 
                            cfg[section][option] = check_path(config.get(section, option))
                        else:
                            sys.exit('The following option {option} in the [{section}] section is missing'.format(section, option))
                    # get user and mastodon instance
                    _, instance = section.split(addressflag)
                    cfg[section]['instance_url'] = 'https://{instance}'.format(instance=instance)
                    cfg[section]['doc_type'] = section
                # elasticsearch configuration parsing only
                if addressflag not in section and 'elasticsearch' == section:
                    cfg[section]['elasticsearch'] = parse_elasticsearch(config)
        cfgs.append(cfg)
    return cfgs

def check_path(filepath):
    if not os.path.exists(filepath):
        sys.exit('The path: {parameter} does not exist.'.format(parameter=filepath))
    elif not os.path.isfile(filepath):
        sys.exit('The path: {parameter} is not a file.'.format(parameter=filepath))
    else:
        return filepath
