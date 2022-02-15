import subprocess
import time


def unistallingaos_commands():


############################################################################################################################
############################################################################################################################


#########################################
# Prepare the system for uninstallation #
#########################################

  def prepare_un_commands():
    pro = subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])

    print(pro.returncode)

    if int(pro.returncode)==0:
        print("#######################################################") 
        print("*             Preparation was successful              *")
        print("#######################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("############################################################################") 
        print("*                   warning: Preparation was was failed                    *")
        print("############################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to Prepare the system to uninstallation again? [y/n]")  
        if loop  == "y":
          prepare_un_commands()
          

  prepare_un_commands()


##############################################################################################################################
##############################################################################################################################


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
          time.sleep(3)

      else:

          print("############################################################################") 
          print("*                      linux-aos-backup was failed                         *")
          print("############################################################################")
          time.sleep(3)
          print("")
          loop = input("Do you want to try to enable linux-aos-backup again? [y/n]")  
          if loop  == "y":
            subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
            timeshift_commands()
            

                  
  timeshift_commands()


##############################################################################################################################
##############################################################################################################################

  
##########################
#    unistalling aos     #
##########################


  def unistalling_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'remove', 'preload', '-y'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'remove', 'prelink', '-y'])
    pro3 = subprocess.run(['sudo', 'apt-get', 'remove', 'gnome-disk-utility', '-y'])
    pro4 = subprocess.run(['sudo', 'apt-get', 'remove', 'nohang', '-y'])
    pro5 = subprocess.run(['sudo', 'apt-get', 'remove', 'fish', '-y'])
    pro6 = subprocess.run(['sudo', 'apt-get', 'remove', 'mesa-utils', '-y'])
    pro7 = subprocess.run(['sudo', 'apt-get', 'remove', 'mesa-utils-extra', '-y'])
    pro8 = subprocess.run(['sudo', 'apt-get', 'remove', 'indicator-cpufreq', '-y'])
    pro9 = subprocess.run(['sudo', 'apt-get', 'remove', 'profile-sync-daemon', '-y'])
    pro10 = subprocess.run(['sudo', 'apt-get', 'remove', 'fakeroot', '-y'])
    pro11 = subprocess.run(['sudo', 'systemctl', 'disable', '--now', 'prelockd.service'])
    pro12 = subprocess.run(['sudo', 'apt-get', 'remove', 'zram-config', '-y'])
    pro13 = subprocess.run(['sudo', 'apt-get', 'remove', 'tlp', '-y'])
    pro14 = subprocess.run(['sudo', 'systemctl', 'disable', '--now', 'memavaild.service'])
    pro15 = subprocess.run(['sudo', 'apt-get', 'remove', 'tuned', 'tuned-utils', 'tuned-utils-systemtap', '-y'])
    pro16 = subprocess.run(['sudo', 'apt-get', 'remove', 'fail2ban', '-y'])
    pro17 = subprocess.run(['sudo', 'ufw', 'disable'])
    pro18 = subprocess.run(['sudo', 'apt-get', 'remove', 'git', '-y'])
    pro19 = subprocess.run(['sudo', 'systemctl', 'disable', 'ananicy'])



    print(pro.returncode)
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


    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode + pro7.returncode + 
       pro8.returncode + pro9.returncode + pro10.returncode + pro11.returncode + pro12.returncode + pro12.returncode + pro14.returncode + 
       pro15.returncode + pro16.returncode + pro17.returncode + pro18.returncode + pro19.returncode)==0:
       print("##########################################################") 
       print("*             unstalling aos was successful              *")
       print("##########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("#####################################################################") 
       print("*                warning: unstalling aos was failed                 *")
       print("#####################################################################")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to unstalling aos again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        unistalling_commands()                

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
    pro4 = subprocess.run(['sudo', 'apt-get', 'install', 'bluez', '-y'])
    pro5 = subprocess.run(['sudo', 'apt-get', 'install', 'xscreensaver', '-y'])
#### return snap if is removed 
    pro6 = subprocess.run(['sudo', 'apt-get', 'install', 'snap', '-y'])    
    pro7 = subprocess.run(['sudo', 'apt-get', 'install', 'snapd', '-y'])


    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro6.returncode)
    print(pro7.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode + pro5.returncode + pro5.returncode +
       pro6.returncode + pro7.returncode)==0:
       print("#########################################################") 
       print("*        return unnecessary tools was successful        *")
       print("#########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("#########################################################################") 
       print("*              warning: return unnecessary tools was failed             *")
       print("#########################################################################")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to return unnecessary tools again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        reunnecessary_commands()        
        

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

    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode)==0:
       print("############################################################") 
       print("*             unstalling aos_ppa was successful            *")
       print("############################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("#########################################################################") 
       print("*                warning: unstalling aos_ppa was failed                 *")
       print("#########################################################################")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to unstalling aos_ppa again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        reppa_commands()        

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
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
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
    pro3 = subprocess.run(['apt-cache', 'policy', 'firefox'])
    print(pro3.returncode)
    
    if int(pro3.returncode)==0:
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
        loop = input("Do you want to try installing firefox before you remove chromium [y/n] ?")
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          rmchromium_commands()


  rmchromium_commands()


####################
# apparmor disable #
####################


  def diapparmor_commands():
####### chek if apparmor enable
   pro0 = subprocess.run(['aa-enabled'])
   print(pro0.returncode)
   if int(pro0.returncode)==0:
    print("")
    print("")
    print("The program has identified apparmor is enable")
    print("")
    disapparmor = input("Do you want to disable apparmor ? [y/n] ")  
    if disapparmor  == "y":

      pro = subprocess.run(['sudo', 'bash', 'scripts/apparmor_disable.sh'])
      pro2 = subprocess.run(['sudo', 'apt-get', 'remove', 'apparmor-easyprof', 'apparmor-notify', 'apparmor-utils', 'certspotter', '-y'])
      pro3 = subprocess.run(['sudo', 'update-grub'])

      print(pro.returncode)
      print(pro2.returncode)
      print(pro3.returncode)
      

      if int(pro.returncode + pro2.returncode + pro3.returncode)==0:
          print("#######################################################") 
          print("*            Successfully disable apparmor            *")
          print("#######################################################")
          print("")
          print("")
          print("the program will continue the installation process in a few seconds, please wait ...")
          time.sleep(3)

      else:

          print("##########################################################################") 
          print("*                      Failed to disable apparmor                        *")
          print("##########################################################################")
          time.sleep(3)
          print("")
          loop = input("Do you want to try to disable apparmor again ? [y/n]")  
          if loop  == "y":
            subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
            diapparmor_commands()

  diapparmor_commands()


#############################
#  autoclean && autoremove  #
#############################


  def autoclean_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'autoclean', '-y'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'auto-remove', '-y'])

    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
       print("###########################################################") 
       print("*         autoclean && autoremove was successful          *")
       print("###########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("##############################################################################") 
       print("*                warning: autoclean && autoremove was failed                 *")
       print("##############################################################################")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to autoclean && autoremove again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        autoclean_commands()
            

  autoclean_commands()


unistallingaos_commands()

print("")
print("For more details")
print("#########################################")
print("https://github.com/ramner98/LINUX-AOS.git")
print("#########################################")
time.sleep(3)
print("")
