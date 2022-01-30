#!bin/bash

cd memavaild-master
sudo deb/build.sh
sudo apt-get install --reinstall ./deb/package.deb
cd ..
sudo systemctl enable --now memavaild.service
sudo systemctl restart --now memavaild.service

