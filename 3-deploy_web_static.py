#!/usr/bin/env python
# using do_pack and do_deploy

from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy
from fabric.api import env, put, run

env.user = "ubuntu"
env.hosts = ["34.75.158.98", "35.229.66.249"]
def deploy():
    """
    making use of do_pack and do_deploy
    """
    packer = do_pack()
    if not packer:
        return False
    deploy = do_deploy(packer)
    return deploy
