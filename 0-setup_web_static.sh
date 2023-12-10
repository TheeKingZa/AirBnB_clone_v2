#!/usr/bin/env bash
# This Script sets up your web servers for the deployment of web_static.

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo -e '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>' | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="location /hbnb_static {\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "/server_name _;/a $nginx_config" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
