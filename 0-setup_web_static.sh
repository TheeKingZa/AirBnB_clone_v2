#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo "<html><head></head><body>Testing Nginx configuration with web_static</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content="
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}
"

echo "$config_content" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart Nginx to apply changes
sudo systemctl restart nginx
