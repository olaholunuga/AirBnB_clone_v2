#!/usr/bin/env python
# cleaning up the remote servers

import os
from fabric.api import *

env.user = "ubuntu"
env.hosts = ["34.75.158.98", "35.229.66.249"]

def do_clean(number=0):
    """
    deletes decrepedated achives from the localhost and the web servers
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("Versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for archive in archives]

    with cd("/data/web_static/releases"):
        rm_archives = run("rm -tr").split()
        rm_archives = [a for a in rm_archives if "web_static_" in a]
        [rm_archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for archive in rm_archives]
