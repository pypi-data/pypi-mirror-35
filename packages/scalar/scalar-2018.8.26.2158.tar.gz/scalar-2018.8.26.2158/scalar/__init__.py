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

import sys
#if sys.version_info[0] <= 2:
#    print("Python >2 required")
#    sys.exit(1)
import docopt
import logging
import mimetypes
if sys.version_info[0] <= 2:
    from pathlib2 import Path
else:
    from pathlib import Path
import yaml

from matrix_client.client import MatrixClient
import technicolor

name        = "scalar"
__version__ = "2018-08-26T2158Z"

log = logging.getLogger(name)
log.addHandler(technicolor.ColorisingStreamHandler())
log.setLevel(logging.DEBUG)
log.debug(name + " " + __version__)

global config
config = None
global client
global token
global room

def setup(path_config="~/.config/scalar/config.yaml", configuration_name=None):
    """
    Load a configuration from a default or specified configuration file, accessing a default or
    specified configuration name.
    """
    global config
    global client
    global token
    global room
    # config file
    path_config = Path(path_config).expanduser()
    log.debug("load config {path}".format(path = path_config))
    if not path_config.exists():
        log.error("no config {path} found".format(path = path_config))
        sys.exit()
    else:
        with open(str(path_config), "r") as _file:
            config = yaml.load(_file)
    if not configuration_name:
        for configuration in list(config["configurations"].items()):
            if configuration[1]["default"]:
                config = configuration[1]
    else:
        config["configurations"][configuration_name]
    # connect to homeserver and room
    log.debug("Matrix username: " + config["username"])
    log.debug("connect to homeserver " + config["homeserver"])
    client = MatrixClient(config["homeserver"])
    token = client.login_with_password(username = config["username"], password = config["passcode"])
    log.debug("connect to room " + config["room_alias"])
    room = client.join_room(config["room_alias"])

def ensure_setup():
    global config
    if not config:
        setup()

def alert(message=None):
    ensure_setup()
    global config
    global options
    options = docopt.docopt(__doc__)
    if not message:
        message = options["--message"]
    log.debug("send message {message} to room {room_alias} on homeserver {homeserver}".format(
        message    = message,
        room_alias = config["room_alias"],
        homeserver = config["homeserver"]
    ))
    send_text(message)

def upload(filepath=None):
    ensure_setup()
    global config
    global client
    global token
    global room
    filepath = Path(filepath).expanduser()
    log.debug("load {path}".format(path = filepath))
    if not filepath.exists():
        log.error("{path} not found".format(path = filepath))
        return False
    with open(str(filepath), "rb") as _file:
        _f = _file.read()
        _b = bytes(bytearray(_f))
    mimetype = mimetypes.guess_type(str(filepath))[0]
    log.debug("upload {path}".format(path = filepath))
    mxc = client.upload(bytes(_b), mimetype)
    result = {
        "filepath": filepath,
        "filename": filepath.name,
        "mimetype": mimetype,
        "url"     : mxc
    }
    log.debug("upload: " + str(result))
    return result

def send_text(text):
    ensure_setup()
    global config
    global client
    global token
    global room
    result = room.send_text(text)
    log.debug("event: " + str(result))

def send_audio(filepath):
    ensure_setup()
    global config
    global client
    global token
    global room
    result = upload(filepath=filepath)
    if result:
        log.debug("send {path}".format(path = filepath))
        result = room.send_audio(result["url"], result["filename"])
        log.debug("event: " + str(result))

def send_file(filepath):
    ensure_setup()
    global config
    global client
    global token
    global room
    result = upload(filepath=filepath)
    if result:
        log.debug("send {path}".format(path = filepath))
        result = room.send_file(result["url"], result["filename"])
        log.debug("event: " + str(result))

def send_image(filepath):
    ensure_setup()
    global config
    global client
    global token
    global room
    result = upload(filepath=filepath)
    if result:
        log.debug("send {path}".format(path = filepath))
        result = room.send_image(result["url"], result["filename"])
        log.debug("event: " + str(result))

def send_video(filepath):
    ensure_setup()
    global config
    global client
    global token
    global room
    result = upload(filepath=filepath)
    if result:
        log.debug("send {path}".format(path = filepath))
        result = room.send_video(result["url"], result["filename"])
        log.debug("event: " + str(result))
