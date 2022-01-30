#!/bin/bash 

git clone https://github.com/Nefelim4ag/Ananicy.git
./Ananicy/package.sh debian
sudo dpkg -i ./Ananicy/ananicy-*.deb
sudo systemctl enable ananicy
sudo systemctl start ananicy
