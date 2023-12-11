#!/usr/bin/python3
"""
Fabric script that distributes an archive
to your web servers using the
function do_deploy.
"""
from fabric.api import env, put, run
from os.path import exists
from datetime import datetime  # Import datetime here

# Update with your web server IP addresses
env.hosts = ['100.26.153.74', '52.86.237.106']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/authorized_keys'


def do_deploy(archive_path):
    """
    Distributes an archive
    to web servers and deploys it.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the server
        put(archive_path, '/tmp/')

        # Extract the archive to
        # /data/web_static/releases/<filename without extension>/
        filename = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/{}'.format(
            filename.split('.')[0]
        )
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))

        # Remove the uploaded archive from the server
        run('rm /tmp/{}'.format(filename))

        # Move contents to the web_static folder
        run('mv {}/web_static/* {}'.format(folder_name, folder_name))

        # Remove the web_static folder created by the extraction
        run('rm -rf {}/web_static'.format(folder_name))

        # Delete the symbolic link /data/web_static/current
        run('rm -f /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print('New version deployed!')
        return True

    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    # Example usage:
    archive_path = "/path/to/your/archive.tgz"
    do_deploy(archive_path)
