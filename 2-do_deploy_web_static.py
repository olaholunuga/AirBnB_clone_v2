#!/usr/bin/env python
# first deploy to servers

from fabric.api import env, put, run
from os.path import exists

env.hosts = ["35.229.66.249", "34.75.158.98"]

def do_deploy(archive_path):
    if not exists(archive_path):
        return False
    try:
        file_path_0 = archive_path.split("/")[-1]
        file_path = file_path_0.split("0")[0]
        put(archive_path, "/tmp/{}.tgz".format(file_path))
        run("mkdir -p /data/web_static/releases/{}/".format(file_path))
        run("tar -xzf /tmp/{0:}.tgz -C /data/web_static/releases/{0:}/".format(file_path))
        run("rm -rf /tmp/{}.tgz".format(file_path))
        run("mv /data/web_static/releases/{0:}/web_static/* /data/web_static/releases/{0:}/".format(file_path))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(file_path))
        return True
    except Exception as err:
        print(err)
