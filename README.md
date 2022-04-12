

###########################################################################################################################################

This tool will download,install and optimize a concept of software and settings.
Its purpose is to optimize the system and make it
Work much faster while maintaining stability.

The concept focuses on optimizing CPU usage, dynamic-virtual-hard memories,responsiveness,power consumption,improving internet usage and speed,system security and in fact the entire operating system.
All comes along with the option to install The excellent kernel liquorix that can upgrade you to a different label of performance or instead you can stay with ubuntu default kernel and still enjoy great performance.
The installer also adds the grub-customizer so you can switch between the kernels whenever you want or if necessary.

It is important to clarify the installation is only for ubuntu-based distributions (this includes mint and similar distro) and only for new and clean systems!
This is because the installation overwrites files and settings on the system.If you still want to install On an existing distribution you will need to perform a full backup of the entire system before that!

I have been using the concept for two years and to this day I have not had any problems but it is worth noting that using an advanced kernels like liquorix can sometimes have an effect on drivers
So you have the option to perform the installation without it or replace it using grub-customizer even after installation.

The tool has been tested on lts distributions 20.04 / 18.04 but should work on any ubuntu based distribution from version 18.04 LTS when the recommendation is to always use LTS versions.

Recommends installing on a light and clean desktop like - xfce or LXDE.

******************************************************************************************************************************************
##########################################################################################################################################


### install


Open a terminal and run the following command

#### $ sudo apt-get update

#### $ sudo apt-get install git

Download the tool to home folder

#### $ git clone https://github.com/ramner98/LINUX-AOS.git

#### $ cd linux-booster && chmod +x install_linux_aos.sh && sudo ./install_linux_aos.sh -yy

or

#### $ cd linux-booster

#### $ chmod +x install_linux_aos.sh

#### $ sudo ./install_linux_aos.sh

##########################################################################################################################################

#### You have two options:

1.Install with the excellent liquorix kernel

2.Install with the default kernel of ubuntu

You will always have the option to use the tool Grub Customizer which is also installed To replace kernel

#########################################################################################################################################

#### To implement profile-sync-daemon optimizations 

#### $ systemctl --user restart psd.service

Check if it is active

#### $ systemctl --user status psd.service

#########################################################################################################################################

#### Use tuned-adm

To choose the profile that can suit your requirements

Enter to list profiles 

#### $ tuned-adm list

Select a profile

#### $ sudo tuned-adm profile {profile name}

Activate the profile

#### $ sudo tuned-adm active

##########################################################################################################################################

### uninstall

1.Run the program and select "Uninstall"
This option will remove most of the installation (not all of it) and try to backup to the existing state by timeshift. 

2.While installing the program, the program will try to perform a backup using a timeshift named
"linux-aos-uninstall". You can select this option to return to the state you were in before installing the program.

#### Warning !!
#### This option will return your entire system (all settings) to the state it was in before installation. 

##########################################################################################################################################

#
#
## System requirements
#

#### Minimum requirements for office use included browser use and video viewing

x64 processor with 1 core

512MB RAM memory + 512MB zram memory

4GB of swap memory on the hard disk

32GB hard disk

LXDE Desktop

#### Minimum requirements for full office use included browser use and video viewing

x64 processor with 1 core

768MB RAM memory + 768MB zram memory

4GB of swap memory on the hard disk

32 GB hard disk

LXDE Desktop

#### Minimum requirements for performing advanced operations such as virtualization

x64 processor with 1 core

2048MB RAM memory + 2048MB zram memory

8GB of swap memory on the hard disk

128 GB hard disk

LXDE or xfce desktop

#
#
#### Note ! 
##### For weak computers is recommended to use liquorix-kernel even if GPU drivers are not supported.
#
#
##### Performance may vary depending on computer hardware,kernel,GPU usage,type and power of computer cooling components.


### Enjoy!
