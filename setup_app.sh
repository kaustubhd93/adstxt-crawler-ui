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
cd redis-5.0.4
echo "*************************************************"
echo "We are in directory : `pwd`"
echo "*************************************************"
make distclean
make
make test
sudo make install
mkdir -p ~/redis/6379
sudo mkdir -p /var/log/redis/
cp redis.conf redis_backup.conf

# Copy redis configuration file from source, make config changes and also setup required directories.
sed -i 's/daemonize no/daemonize yes/g' redis.conf
sed -i 's/logfile ""/logfile \/var\/log\/redis\/redis_6379.log/g' redis.conf
sed -i "s/dir .\//dir \/home\/`whoami`\/redis\/6379/" redis.conf
sudo mkdir -p /etc/redis
sudo cp redis.conf /etc/redis/
sudo redis-server /etc/redis/redis.conf &
cd ../adstxt-crawler-ui
echo "*************************************************"
echo "We are in directory : `pwd`"
echo "*************************************************"

# Install Rabbitmq using it's script.
bash scripts/setup-rabbitmq.sh

# Take input for passwd user for credentials of rabbitmq
# Setup user, passwd and virtual host for rabbitmq.
passwd=`/bin/whiptail --inputbox "Please enter password for rabbitmq virtual host. Please remember this passwd" 8 50 $prefill 3>&1 1>&2 2>&3`
sudo rabbitmqctl add_user adstxt $passwd
sudo rabbitmqctl add_vhost adstxtcrawler
sudo rabbitmqctl set_user_tags adstxt adstxttags
sudo rabbitmqctl set_permissions -p adstxtcrawler adstxt ".*" ".*" ".*"

# Create virtual environment
mkdir -p ~/.virtualenvs
python3.5 -m venv ~/.virtualenvs/adstxt

# Activate virtual env.
source ~/.virtualenvs/adstxt/bin/activate

# Install all supporting python libraries
pip install wheel
pip install -U pip
pip install -r requirements.txt

# Run dameon scripts to start app_server and rabbitmq workers accordingly.
