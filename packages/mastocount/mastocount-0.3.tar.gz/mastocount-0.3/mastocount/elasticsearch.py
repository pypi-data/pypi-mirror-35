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

# Feed the ElasticSearch database
'''Feed the ElasticSearch Databases'''

from datetime import datetime
from elasticsearch import Elasticsearch

def feed(escfg, followers):
    '''Feed the database'''
    es = Elasticsearch()
    for follower in followers:
        doc = {
            follower: followers[follower] ,
            'timestamp': datetime.now(),
        }
        res = es.index(index=escfg['elasticsearch']['index'], doc_type='followers', body=doc)
