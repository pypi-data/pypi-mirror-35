#!/usr/bin/env python3
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
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

'''Checks an RSS feed, format it, store it and posts new entries to the social networks.'''

# standard libraires imports
import sys

# 3rd party libraries imports
import feedparser

# app libraries imports
from mastocount.cliparse import cliparse
from mastocount.cfgparse import cfgparse
from mastocount.elasticsearch import feed
from mastocount.followers import get_followers
from mastocount.prettyprint import pretty_print
from mastocount.total import get_total

class Main:
    '''Main class of Mastocount'''

    def __init__(self):
        self.main()

    def main(self):
        '''The main function'''
        clioptions = cliparse()
        cfgs = cfgparse(clioptions)
        for cfg in cfgs:
            followers = get_followers(cfg)
            followers = get_total(followers)
            pretty_print(followers)
        sys.exit(0)
