#!/bin/bash

# Updating repository
sudo apt update

# Install build-essential and git
# Install mysql and mysql libraries for python client
sudo apt install vim build-essential git mysql-server libmysqlclient-dev python3.5-dev python3.5-venv tcl

# Run mysql secure installation

# Create user and db for Django in Mysqldb

# Install redis and run make stuff
wget http://download.redis.io/releases/redis-5.0.4.tar.gz
tar -xvf redis-5.0.4.tar.gz
cd redis-5.0.4.tar
make distclean
make
make test
sudo make install

# Copy redis configuration file from source, make config changes and also setup required directories.

# Install Rabbitmq using it's script.
bash scripts/setup-rabbitmq.sh

# Take input for passwd user for credentials of rabbitmq

# Setup user, passwd and virtual host for rabbitmq.
sudo rabbitmqctl add_user $username $passwd
sudo rabbitmqctl add_vhost $virthost
sudo rabbitmqctl set_user_tags $username $tag
sudo rabbitmqctl set_permissions -p $virthost $username ".*" ".*" ".*"

# Run dameon scripts to start app_server and rabbitmq workers accordingly.
