#!/usr/bin/env python
# put the contents of web_static inti a compressed archive

from fabric.api import local
from datetime import datetime

def do_pack():
    #local("mkdir versions")
    dt = datetime.utcnow()
    file_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    if local("tar -cvzf {} web_static".format(file_path)).failed is True:
        return None

    return file_path
