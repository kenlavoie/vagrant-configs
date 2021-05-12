#!/usr/bin/env bash
#export UCP_PUBLIC_IP = ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'
apt-get update
apt-get -y install curl
apt-get -y install nginx
cp dockah-vhost.conf /etc/nginx/sites-available
sudo ln-s /etc/nginx/sites-available/
sudo service nginx restart
