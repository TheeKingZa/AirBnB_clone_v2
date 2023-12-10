#!/usr/bin/env python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Archive path if generated successfully, None otherwise.
    """
    try:
        # Create the 'versions' folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive filename with the current date and time
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

        # Compress the web_static folder into the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if successful
        return "versions/{}".format(archive_name)

    except Exception as e:
        # Print an error message and return None if an exception occurs
        print("Error: {}".format(e))
        return None

# Run the script using 'fab -f 1-pack_web_static.py do_pack'
