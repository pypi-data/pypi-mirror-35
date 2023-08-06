# -*- coding: utf-8 -*-
# Copyright © 2018 Carl Chenet <carl.chenet@ohmytux.com>
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

# Get values of the elasticsearch section
'''Get values of the elasticsearch section'''

# standard library imports
import os.path
import sys

def parse_elasticsearch(config):
    '''Parse configuration values and get values of the elasticsearch section'''
    cfg = {}
    section = 'elasticsearch'
    ####################################
    # media option
    ####################################
    cfgoption = 'index'
    if config.has_section(section):
        if config.has_option(section, cfgoption):
            cfgvalue = config.get(section, cfgoption)
        cfg[cfgoption] = cfgvalue
    return cfg
