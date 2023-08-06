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

# Get followers from Mastodon
'''Get followers from Mastodon'''

# standard libraries imports
import os.path
import sys

# 3rd party libraries imports
from mastodon import Mastodon

# local imports
from mastocount.elasticsearch import feed

def get_followers(cfg):
    '''Use Mastodon credentials to get the the number of followers'''
    mastodonresults = {}
    usercounts = {}
    for credential in cfg:
        if 'elasticsearch' != credential:
            mastodon = Mastodon(
                client_id=cfg[credential]['client_credentials'],
                access_token=cfg[credential]['user_credentials'],
                api_base_url=cfg[credential]['instance_url']
            )
            userid = mastodon.account_verify_credentials()['id']
            usercounts[credential] = mastodon.account(userid).followers_count
            mastodonresults[credential] = mastodon.account(userid).followers_count
    for credential in cfg:
        if 'elasticsearch' == credential:
            feed(cfg['elasticsearch'], usercounts)
            usercounts = {}
    return mastodonresults
