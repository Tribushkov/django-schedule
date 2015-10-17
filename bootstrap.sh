#! /usr/bin/env bash

# Variables
DBNAME=db
DBUSER=root

echo -e "\n--- Installing now... ---\n"

echo -e "\n--- Updating packages list ---\n"
apt-get -qq update

echo -e "\n--- Installing base packages ---\n"
apt-get -y install vim curl git python-pip > /dev/null 2>&1

echo -e "\n--- Installing python packages ---\n"
pip -q install django django-registration-redux> /dev/null 2>&1

echo -e "\n--- Installing MySQL specific packages and settings ---\n"
echo "mysql-server mysql-server/root_password password $DBPASSWD" | debconf-set-selections
echo "mysql-server mysql-server/root_password_again password $DBPASSWD" | debconf-set-selections
apt-get -y install mysql-server > /dev/null 2>&1

echo -e "\n--- Done! ---\n"