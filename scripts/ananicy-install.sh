#!/bin/bash 

git clone https://github.com/Nefelim4ag/Ananicy.git /tmp/ananicy
cd /tmp/ananicy
sudo make install
sudo systemctl enable ananicy
sudo systemctl start ananicy
