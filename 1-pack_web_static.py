#!/usr/bin/python3
"""
Fabric script that generates a .tgz from the contents of web_static
"""
from fabric.api import local
import time


def do_pack():
    """
        Return the archive path if archive has been correctly
        gernerated.
    """

    local('mkdir -p versions')
    date = time.strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(file_name))

    if t_gzip_archive:
        return file_name
    return None
