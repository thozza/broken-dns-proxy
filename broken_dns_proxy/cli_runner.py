# -*- coding: utf-8 -*-
#
# Simple DNS Proxy for simulating DNS issues
# Copyright (C) 2014-2015  Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:

import sys

from broken_dns_proxy.arguments_parser import ArgumentsParser
from broken_dns_proxy.application import Application
from broken_dns_proxy.logger import logger
from broken_dns_proxy.exceptions import BrokenDNSProxyError


class CliRunner(object):
    """
    Entry point class for command line
    """

    @staticmethod
    def run():
        try:
            args = ArgumentsParser(sys.argv[1:])
            app = Application(args)
            app.run()
        except KeyboardInterrupt:
            logger.info('\nInterrupted by user')
        except BrokenDNSProxyError as e:
            logger.error('\n{0}'.format(e))
            sys.exit(1)

        sys.exit(0)