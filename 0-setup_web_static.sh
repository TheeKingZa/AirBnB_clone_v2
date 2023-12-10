#!/usr/bin/env bash
# install nginx and make folders

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get -y update
    apt-get -y install nginx
fi

# Create necessary folders
folders=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")
for folder in "${folders[@]}"; do
    mkdir -p "$folder"
done

# Create a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_block="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n"
sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart