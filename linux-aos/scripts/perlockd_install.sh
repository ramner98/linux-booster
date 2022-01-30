#!bin/bash

cd prelockd-master
sudo make install
sudo systemctl enable --now prelockd.service
sudo systemctl restart  prelockd

cd ..
