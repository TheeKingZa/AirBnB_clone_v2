#!/bin/bash
# install nginx and make folders

# Check for root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root or with sudo."
    exit 1
fi

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update && sudo apt-get -y install nginx
fi

# Create necessary folders
folders=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/" "/data/web_static/releases/test/")
for folder in "${folders[@]}"; do
    sudo mkdir -p "$folder" && echo "Created $folder"
done

# Create a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R $USER:$USER /data/

# Update Nginx configuration
config_block="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
