#! /usr/bin/python

#  Copyright 2013 Linaro Limited
#  Author Matt Hart <matthew.hart@linaro.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import logging


class NoDriverException(Exception):
    pass


class PDUDriver(object):
    connection = None
    firmware_dict = {}

    def __init__(self, connection):
        self.connection = connection

        # return the driver that provides the firmware version
    def _port_interaction(self, command, port_number):
        pass

    def _pdu_logout(self):
        pass

    def port_on(self, port_number):
        self._port_interaction("on", port_number)

    def port_off(self, port_number):
        self._port_interaction("off", port_number)