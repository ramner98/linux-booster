import subprocess
import time


def unistallingaos_commands():


############################################################################################################################
############################################################################################################################


####################
# linux-aos-backup #
####################

  def timeshift_commands():
  
      pro = subprocess.run(['sudo', 'timeshift', '--create', '--comments', 'linux-aos-backup'])
      print(pro.returncode)

      if int(pro.returncode)==0:
          print("#######################################################") 
          print("*           linux-aos-backup was successful           *")
          print("#######################################################")
          print("")
          print("")
          print("the program will continue the installation process in a few seconds, please wait ...")
          time.sleep(5)

      else:

          print("############################################################################") 
          print("*                      linux-aos-backup was failed                         *")
          print("############################################################################")
          time.sleep(3)
          print("")
          loop = input("Do you want to try to enable linux-aos-backup again? [y/n]")  
          if loop  == "y":
            timeshift_commands()

                  
  timeshift_commands()


##############################################################################################################################
##############################################################################################################################

  
##########################
#    unistalling aos     #
##########################


  def unistalling_commands():
    pro2 = subprocess.run(['sudo', 'apt-get', 'remove', 'preload', '-y'])
    pro3 = subprocess.run(['sudo', 'apt-get', 'remove', 'prelink', '-y'])
    pro4 = subprocess.run(['sudo', 'apt-get', 'remove', 'gnome-disk-utility', '-y'])
    pro5 = subprocess.run(['sudo', 'apt-get', 'remove', 'nohang', '-y'])
    pro6 = subprocess.run(['sudo', 'apt-get', 'remove', 'fish', '-y'])
    pro7 = subprocess.run(['sudo', 'apt-get', 'remove', 'mesa-utils', '-y'])
    pro8 = subprocess.run(['sudo', 'apt-get', 'remove', 'mesa-utils-extra', '-y'])
    pro9 = subprocess.run(['sudo', 'apt-get', 'remove', 'indicator-cpufreq', '-y'])
    pro10 = subprocess.run(['sudo', 'apt-get', 'remove', 'profile-sync-daemon', '-y'])
    pro11 = subprocess.run(['sudo', 'apt-get', 'remove', 'fakeroot', '-y'])
    pro12 = subprocess.run(['sudo', 'systemctl', 'disable', '--now', 'prelockd.service'])
    pro13 = subprocess.run(['sudo', 'apt-get', 'remove', 'zram-config', '-y'])
    pro14 = subprocess.run(['sudo', 'apt-get', 'remove', 'tlp', '-y'])
    pro15 = subprocess.run(['sudo', 'apt-get', 'remove', 'tlpui', '-y'])
    pro16 = subprocess.run(['sudo', 'systemctl', 'disable', '--now', 'memavaild.service'])
    pro17 = subprocess.run(['sudo', 'apt-get', 'remove', 'tuned', 'tuned-utils', 'tuned-utils-systemtap', '-y'])
    pro18 = subprocess.run(['sudo', 'apt-get', 'remove', 'fail2ban', '-y'])
    pro19 = subprocess.run(['sudo', 'ufw', 'disable'])
    pro20 = subprocess.run(['sudo', 'apt-get', 'remove', 'git', '-y'])
    pro21 = subprocess.run(['sudo', 'systemctl', 'disable', 'ananicy'])



    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro6.returncode)
    print(pro7.returncode)
    print(pro8.returncode)
    print(pro9.returncode)
    print(pro10.returncode)
    print(pro11.returncode)
    print(pro12.returncode)
    print(pro13.returncode)
    print(pro14.returncode)
    print(pro15.returncode)
    print(pro16.returncode)
    print(pro17.returncode)
    print(pro18.returncode)
    print(pro19.returncode)
    print(pro20.returncode)
    print(pro21.returncode)


    if int(pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode + pro7.returncode + 
       pro8.returncode + pro9.returncode + pro10.returncode + pro11.returncode + pro12.returncode + pro12.returncode + pro14.returncode + 
       pro15.returncode + pro16.returncode + pro17.returncode + pro18.returncode + pro19.returncode + pro20.returncode + pro21.returncode)==0:
       print("##########################################################") 
       print("*             unstalling aos was successful              *")
       print("##########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(5)
            

  unistalling_commands()  

##############################################################################################################################
##############################################################################################################################


############################
# return unnecessary tools #
############################


  def reunnecessary_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'update-notifier', '-y'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'install', 'thunderbird', '-y'])
    pro3 = subprocess.run(['sudo', 'apt-get', 'install', 'gnome-software', '-y'])


    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)

 
    if int(pro.returncode + pro2.returncode + pro3.returncode)==0:
       print("#########################################################") 
       print("*        return unnecessary tools was successful        *")
       print("#########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)
            

  reunnecessary_commands()  


############################################################################################################################
############################################################################################################################


##########################
# remove unnecessary ppa #  
##########################


  def reppa_commands():

    pro = subprocess.run(['sudo', 'add-apt-repository', '--remove', 'ppa:damentz/liquorix', '-yy'])
    pro2 = subprocess.run(['sudo', 'add-apt-repository', '--remove', 'ppa:oibaf/test', '-yy'])
    pro3 = subprocess.run(['sudo', 'add-apt-repository', '--remove', 'ppa:linuxuprising/apps', '-yy'])
    pro4 = subprocess.run(['sudo', 'add-apt-repository', '--remove', 'ppa:system76/pop', '-yy'])
    pro5 = subprocess.run(['sudo', 'add-apt-repository', '--remove', 'ppa:fish-shell/release-3', '-yy'])
    pro6 = subprocess.run(['sudo', 'add-apt-repository', '--remove', 'ppa:system76/pop', '-yy'])

    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro6.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode)==0:
       print("##########################################################") 
       print("*             unstalling aos was successful              *")
       print("##########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(5)
            

  reppa_commands()  


############################################################################################################################
############################################################################################################################


##########################
# Return important files #
##########################


  def returnup_commands():
    pro = subprocess.run(['sudo', 'cp', 'backup/sysctl.conf', '/etc/sysctl.conf'])
    pro2 = subprocess.run(['sudo', 'cp', 'backup/grub', '/etc/default/grub'])
    pro3 = subprocess.run(['sudo', 'cp', 'backup/hdparm.conf', '/etc/hdparm.conf'])
    pro4 = subprocess.run(['sudo', 'cp', 'backup/modules', '/etc/initramfs-tools/modules'])
    pro5 = subprocess.run(['sudo', 'update-grub'])



    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
 
    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode)==0:
       print("#########################################################") 
       print("*        return important files was successful          *")
       print("#########################################################")
       print("")
       time.sleep(3)

    else:

       print("#############################################################################") 
       print("*                warning: return important files was failed                 *")
       print("#############################################################################")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to return important files again? [y/n]")  
       if loop  == "y":
        returnup_commands()
            

  returnup_commands()  


############################################################################################################################
############################################################################################################################


###################
# remove chromium #
###################


  def rmchromium_commands():
######### check if firefox is installed
    pro = subprocess.run(['sudo', 'apt-get', 'update']) 
    pro2 = subprocess.run(['sudo', 'apt-get', 'install', 'firefox', '-y'])

    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("#########################################################") 
        print("*          firefox is installed in the system           *")
        print("#########################################################")
        print("")
        time.sleep(3)
        rmchromium = input("Do you want to remove chromium ? [y/n]")  
        if rmchromium  == "y":
          subprocess.run(['sudo', 'apt-get', 'remove', 'chromium', '-y'])
          subprocess.run(['sudo', 'apt-get', 'purge', 'chromium', '-y'])
        print("")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("###########################################################################") 
        print("*             warning: firefox is not installed in the system             *")
        print("###########################################################################")
        time.sleep(3)
        print("")
        print("If you choose, *no* ,the program will continue without removing chromium")
        print("so that there will be no situation where you will be left without a browser.")
        print("")
        loop = input("Do you want to try to installing firefox again before you remove chromium [y/n] ?")
        if loop  == "y":
          rmchromium_commands()


  rmchromium_commands()


unistallingaos_commands()

print("")
print("Uninstallation complete.please reboot the system")
print("")
