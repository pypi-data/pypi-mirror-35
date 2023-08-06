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

# Pretty print the number of users
'''Pretty print the number of users'''

import os

def pretty_print(users):
    '''Pretty print the number of users'''
    # get the max length of the user name
    maxlength = 0
    userline = '{linesep}'.format(linesep=os.linesep)
    for user in users:
        newmaxlength = len(user)
        if newmaxlength > maxlength:
            maxlength = newmaxlength
    for user in users:
        if user != 'total':
            userline += '{user}:{space}{count}{linesep}'.format(user=user, space=' '*(1 + maxlength - len(user)), count=users[user], linesep=os.linesep)
    userline += '{linesep}total:{space}{count}{linesep}'.format(linesep=os.linesep, space=' '*(1 + maxlength - len(user)), count=users['total'])
    print(userline)
