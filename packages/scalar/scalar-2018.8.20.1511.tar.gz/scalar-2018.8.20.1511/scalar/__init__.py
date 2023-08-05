"""
################################################################################
#                                                                              #
# scalar                                                                       #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# The program is a Python Matrix library.                                      #
#                                                                              #
# copyright (C) 2018 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

usage:
    program [options]

options:
    -h,--help       display help message
    --version       display version and exit
    --message=TEXT  alert message [default: alert]
"""

name        = "scalar"
__version__ = "2018-08-20T1511Z"

import sys
if sys.version_info[0] <= 2:
    print("Python >2 required")
    sys.exit(1)
import docopt
import logging
from pathlib import Path
import yaml

from matrix_client.client import MatrixClient
import technicolor

name        = "scalar"
__version__ = "2018-08-17T1645Z"

log = logging.getLogger(name)
log.addHandler(technicolor.ColorisingStreamHandler())
log.setLevel(logging.DEBUG)

log.debug(name + " " + __version__)
# configuration
path_config = Path("~/.config/scalar/config.yaml").expanduser()
log.debug("load config file {path}".format(path = path_config))
if not path_config.exists():
    log.error("no config file {path} found".format(path = path_config))
    sys.exit()
else:
    with open(str(path_config), "r") as _file:
        config = yaml.load(_file)
# connect to homeserver and room
log.debug("Matrix username: " + config["username"])
log.debug("connect to homeserver " + config["homeserver"])
client = MatrixClient(config["homeserver"])
token = client.login_with_password(username = config["username"], password = config["passcode"])
log.debug("connect to room " + config["room_alias"])
room = client.join_room(config["room_alias"])

def alert(message=None):
    global options
    options = docopt.docopt(__doc__)
    if not message:
        message = options["--message"]
    log.debug("send message {message} to room {room_alias} on homeserver {homeserver}".format(
        message    = message,
        room_alias = config["room_alias"],
        homeserver = config["homeserver"]
    ))
    result = room.send_text(message)
    log.debug("event: " + str(result))
