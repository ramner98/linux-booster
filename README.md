
LINUX-AOS (Automatic Optimization System)

###########################################################################################################################################

This tool will download,install and optimize a concept of software and settings.
Its purpose is to optimize the system and make it
Work much faster while maintaining stability.

The concept focuses on optimizing CPU usage, dynamic-virtual-hard memories,responsiveness,power consumption,Improving Internet usage and speed,system security and in fact the entire operating system.
all comes along with the option to install The excellent kernel liquorix that can upgrade you to a different label of performance or instead you can stay with Ubuntu default kernel and still enjoy great performance.
The installer also adds the grub-customizer so you can switch between the kernels whenever you want or if necessary.

It is important to clarify The installation is only for ubuntu-based distributions (this includes Mint and similar distro) and only for new and clean systems!
This is because the installation overwrites files and settings on the system.If you still want to install On an existing distribution you will need to perform a full backup of the entire system before that!

I have been using the concept for a year and to this day I have not had any problems but it is worth noting that using an advanced kernels like liquorix can sometimes have an effect on drivers
so you have the option to perform the installation without it or replace it using grub-customizer even after installation.

The tool has been tested on lts distributions 20.04 / 18.04 but should work on any ubuntu based distribution from version 18.04 LTS when the recommendation is to always use LTS versions.

Recommends installing on a light and clean desktop like - xfce or LXDE.

******************************************************************************************************************************************
##########################################################################################################################################


Who is it for?

Well...

1.For anyone who wants to utilize his system in a much better way.

2.For people or companies who want to avoid upgrading computers at home or in business to newer
computers and thus save money and get better performance and a higher level of security. 

3.Anyone who wants to preserve the environment, this is because reusing old computers (recycling) can prevent overproduction of new computers,
reduce the dumping of old computers in the trash and thus helps a lot in preserving the environment.

4.Graphic artists or gamers on Linux systems (a topic that is starting to gain increasing popularity in recent years).

5.Code developers,ethical hackers,devops, or scientists who need a large number of virtual machines to learn or experiment.

But the most important reason for me is
To provide a technological solution to people living in Third World countries like many countries in Asia and Africa.
In these places whoever gets to own a computer will usually get a weak, average or old computer,
And this program will definitely be able to make their lives a lot easier for the reason that they can get a lot more out of their system.


##########################################################################################################################################

install


Open a terminal and run the following command

$ sudo apt-get update

$ sudo apt-get install git

Download the tool to home folder

$ git clone https://github.com/ramner98/LINUX-AOS.git

$ cd LINUX-AOS && chmod +x install_linux_aos.sh && sudo ./install_linux_aos.sh -yy

or

$ cd LINUX-AOS

$ chmod +x install_linux_aos.sh

$ sudo ./install_linux_aos.sh

##########################################################################################################################################

You have three options:

1.Install with the excellent liquorix kernel

2.Install with the default kernel of Ubuntu

You will always have the option to use the tool Grub Customizer which is also installed To replace kernel

#########################################################################################################################################

To implement profile-sync-daemon optimizations 

$ systemctl --user restart psd.service

Check if it is active

$ systemctl --user status psd.service

#########################################################################################################################################

Use tuned-adm

To choose the profile that can suit your requirements
Enter to list profiles 

$ tuned-adm list
Select a profile

$ sudo tuned-adm profile {profile name}
Activate the profile

$ sudo tuned-adm active

##########################################################################################################################################

uninstall

1.Run the program and select "Uninstall"
This option will remove most of the installation (not all of it) and try to backup to the existing state by timeshift. 

2.While installing the program, the program will try to perform a backup using a timeshift named
"linux-aos-uninstall". You can select this option to return to the state you were in before installing the program.

Warning !!
This option will return your entire system (all settings) to the state it was in before installation. 

##########################################################################################################################################

Enjoy!


