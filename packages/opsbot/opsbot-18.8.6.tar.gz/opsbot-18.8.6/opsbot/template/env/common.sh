echo "update apt for lastest package ..."
apt update

echo "install goaccess for reading log ..."
apt install -y goaccess

echo "update lastest for the most important tools ..."
apt install -y git
apt install -y python