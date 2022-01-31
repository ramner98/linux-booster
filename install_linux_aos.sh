#!/bin/bash


chmod +x liquorix_install.py
chmod +x ubuntu_install.py
chmod +x uninstall.py
chmod +x config-files/init-zram-swapping
chmod +x scripts/memavaild_install.sh
chmod +x scripts/perlockd_install.sh
chmod +x scripts/ananicy-install.sh


######check for missing and broken packages and repair if necessary.
sudo apt-get --fix-broken install -y
sudo apt-get update --fix-missing
sudo dpkg --configure -a
sudo apt-get install -f
######check if python3.8 is installed
sudo apt-get install python3.8 -y 
######
sudo apt-get install make
######
sudo apt-get install dialog

HEIGHT=15
WIDTH=76
CHOICE_HEIGHT=4
BACKTITLE=""
TITLE="LINUX-AOS(Automatic Optimization System)"
MENU="Choose one of the following options:"

OPTIONS=(1 "Install with liquorix-kernel(Gives high performance to all users)"
         2 "Install with ubuntu-kernel(Strong stability with drivers)"
         3 "Uninstall")

CHOICE=$(dialog --clear \
                --backtitle "$BACKTITLE" \
                --title "$TITLE" \
                --menu "$MENU" \
                $HEIGHT $WIDTH $CHOICE_HEIGHT \
                "${OPTIONS[@]}" \
                2>&1 >/dev/tty)

clear
case $CHOICE in
        1)
            sudo python3 liquorix_install.py
            echo "###################################################"
	        echo "Installation complete please reboot your system"
            echo "###################################################"
             sleep 3
                exit
            ;;
        2)
            sudo python3 ubuntu_install.py
            echo "###################################################"
	        echo "Installation complete please reboot your system"
            echo "###################################################"
             sleep 3
                exit
            ;;

        3)
            sudo python3 uninstall.py
            echo "##########################################################"
            echo       "uninstall completed, please reboot the system"
            echo "##########################################################"
             sleep 3
               exit 
            ;;
esac
