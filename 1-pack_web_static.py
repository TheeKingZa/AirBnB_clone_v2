#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder.
"""

from fabric.api import local, run
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from
    the web_static folder.
    """
    local("git pull origin master")
    local("python manage.py migrate")
    local("python manage.py collectstatic --noinput")
    run("sudo service guicorn")
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the archive filename
    now = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Compress web_static into the archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.succeeded:
        return os.path.abspath("versions/{}".format(archive_name))
    else:
        return None


if __name__ == "__main__":
    do_pack()
