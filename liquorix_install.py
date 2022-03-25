import subprocess
import time



def aos_liquorix_commands():

##############################################################################################################################
##############################################################################################################################


############################
#  Backup important files  #
############################


  def backup_commands():
    pro = subprocess.run(['sudo', 'mkdir', '-p', 'backup/'])
    pro2 = subprocess.run(['sudo', 'cp', '-n', '/etc/sysctl.conf', 'backup/'])
    pro3 = subprocess.run(['sudo', 'cp', '-n',  '/etc/default/grub', 'backup/'])
    pro4 = subprocess.run(['sudo', 'cp', '-n',  '/etc/hdparm.conf', 'backup/'])
    pro5 = subprocess.run(['sudo', 'cp', '-n',  '/etc/initramfs-tools/modules', 'backup/'])


    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)

 
    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode)==0:
       print("##########################################################") 
       print("*         Backup important files was successful          *")
       print("##########################################################")
       print("")
       print("Important files will be backed up only once, even if you run the")
       print("program several more times. This is in order to allow the program to")
       print("uninstall if you choose to do so in the future without using timeshift.")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("#############################################################################") 
       print("*                warning: Backup important files was failed                 *")
       print("#############################################################################")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to Backup important files again? [y/n]")  
       if loop  == "y":
        backup_commands()
            

  backup_commands() 


##############################################################################################################################
##############################################################################################################################


#########################
# system update/upgrade #
#########################


  def update_commands():
        pro = subprocess.run(['sudo', 'apt-get', 'update'])
        pro2 = subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])

        print(pro.returncode)
        print(pro2.returncode)

        if int(pro.returncode + pro2.returncode)==0:
            print("################################")
            print("* system update was successful *")
            print("################################")
            print("")
            print("the program will continue the installation process in a few seconds, please wait ...")
            time.sleep(3)
        else:
            print("#####################################################") 
            print("*          warning: update/upgrade failed           *")
            print("#####################################################")
            print("")
            time.sleep(3)
            print("#####################################################")
            print("Please check if the internet connection is")
            print("available or go to software & updates and select the")
            print("server that suits your area and refresh the service,")
            print("try to install the program again afterwards.")
            print("#####################################################")
            print("")
            loop = input("Do you want to try to update/upgrade again? [y/n]")  
            if loop  == "y":
              subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
              update_commands()


            else:
                
                  print("###############################################################################") 
                  print("*                   warning: update/upgrade was failed again                  *")
                  print("###############################################################################")
                  time.sleep(3)
                  print("")
                  print("You must run this command before the installation begins !")
                  time.sleep(3)

                  quit()
            

  update_commands()


##############################################################################################################################
##############################################################################################################################


###########################################
# Install timeshift and backup the system #
###########################################


  def timeshift_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'timeshift'])
    pro2 = subprocess.run(['sudo', 'timeshift', '--create', '--comments', 'uninstall-LINUX-AOS'])
    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("############################################################")
        print("* Timeshift installation and system backup were successful *")
        print("############################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)
    else:
        print("#####################################################") 
        print("*          warning:system backup is failed          *")
        print("#####################################################")
        print("")
        time.sleep(3)
        print("#################################################################")
        print("Please check if the internet connection is available")
        print("Without installing this software and performing the backup you" )
        print("will not be able to uninstall the program and return to the state")
        print("you were in before the installation.")
        print("#################################################################")
        print("")
        loop = input("Do you want to try to Install timeshift and backup the system again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          timeshift_commands()


        else:
            
              print("##############################################################################") 
              print("*                       warning: backup system failed                        *")
              print("##############################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without backup system? [y/n]") == "n":
                exit ()
          

  timeshift_commands()


##############################################################################################################################
##############################################################################################################################


####################
# git installation #
####################


  def git_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'git', '-y'])
    print(pro.returncode)
    if int(pro.returncode)==0:
        print("###################################")
        print("* git installation was successful *")
        print("###################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)
    else:
        print("########################################") 
        print("* warning: git installation was failed *")
        print("########################################")
        time.sleep(3)
        print("")
        print("##################################################################")
        print("Please check if the internet connection is available and try again")
        print("##################################################################")
        print("")
        loop = input("Do you want to try to install git again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          git_commands()


        else:
            
              print("###############################################################################") 
              print("*                    warning: Installing git was failed                       *")
              print("###############################################################################")
              time.sleep(3)
              print("")
              while input("Do you want to continue without Installing git? [y/n]") == "n":
                exit ()
            

  git_commands()

##############################################################################################################################
##############################################################################################################################


##############################
# Installing liquorix kernel #
##############################


  def liquorix_commands():
    pro = subprocess.run(['sudo', 'add-apt-repository', 'ppa:damentz/liquorix', '-yy'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'update'])
    pro3 = subprocess.run(['sudo', 'apt-get', 'install', 'linux-image-liquorix-amd64', 'linux-headers-liquorix-amd64', '-yy'])
    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode)==0:
        print("#############################################") 
        print("* Installing liquorix kernel was successful *")
        print("#############################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("##################################################") 
        print("* warning: Installing liquorix kernel was failed *")
        print("##################################################")
        time.sleep(3)
        print("")
        print("##############################################################################")
        print("Please check if the internet connection is available and try again")
        print("It is possible that thre developer has changed installation-related commands.")
        print("You can visit the developer website and try to fix the error")
        print("https://liquorix.net/")
        print("##############################################################################")
        print("")
        loop = input("Do you want to try to installing liquorix kernel again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          liquorix_commands()


        else:
            
              print("################################################################################") 
              print("*               warning: Installing liquorix kernel was failed                 *")
              print("################################################################################")
              print("")
              print("Since this installation is designed to run in conjunction with")
              print("the liquorix kernel it will be unnecessary to continue with the program.")
              time.sleep(3)
              exit ()
         

  liquorix_commands()


##############################################################################################################################
##############################################################################################################################


################################
# Install and optimize preload #
################################


  def preload_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'preload'])
    pro2 = subprocess.run(['sudo', 'cp', 'config-files/preload.conf', '/etc/preload.conf'])
    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("##################################################") 
        print("* Installing and optimize preload was successful *")
        print("##################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("#######################################################") 
        print("* warning: Installing and optimize preload was failed *")
        print("#######################################################")
        time.sleep(3)
        print("")
        print("##############################################################################")
        print("Please check if the internet connection is available and try again")
        print("##############################################################################")
        print("")
        loop = input("Do you want to try to install preload again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          preload_commands()


        else:
            
              print("###############################################################################") 
              print("*                   warning: Installing preload was failed                    *")
              print("###############################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without Installing preload? [y/n]") == "n":
                exit ()
          

  preload_commands()


##############################################################################################################################
##############################################################################################################################


################################
# Install and optimize prelink #
################################

  def prelink_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'prelink', '-y'])
    pro2 = subprocess.run(['sudo', 'cp', 'config-files/prelink', '/etc/default/prelink'])
    pro3 = subprocess.run(['sudo', '/etc/cron.daily/prelink'])
    pro4 = subprocess.run(['sudo', 'cp', 'config-files/70debconf', '/etc/apt/apt.conf.d/70debconf'])
    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode)==0:
        print("##################################################") 
        print("* Installing and optimize prelink was successful *")
        print("##################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("#######################################################") 
        print("* warning: Installing and optimize prelink was failed *")
        print("#######################################################")
        time.sleep(3)
        print("")
        print("##############################################################################")
        print("Please check if the internet connection is available and try again")
        print("##############################################################################")
        print("")
        loop = input("Are you interested in trying to install prelink again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          prelink_commands()


        else:
            
              print("###############################################################################") 
              print("*                   warning: Installing prelink was failed                    *")
              print("###############################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without Installing prelink? [y/n]") == "n":
                exit ()

  prelink_commands()


##############################################################################################################################
##############################################################################################################################


#################################
#     Optimize sysctl.conf      #
#################################


  def sysctl_commands():
    pro = subprocess.run(['sudo', 'cp', 'config-files/sysctl.conf', '/etc/sysctl.conf'])
    print(pro.returncode)

    if int(pro.returncode)==0:
        print("##################################################") 
        print("*      optimize sysctl.conf was successful       *")
        print("##################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("#######################################################") 
        print("*      warning: optimize sysctl.conf was failed       *")
        print("#######################################################")
        time.sleep(3)
        print("")
        print("###############################################################################")
        print("It is important to make this change to ensure system optimization is successful")
        print("###############################################################################")
        print("")
        loop = input("Do you want to try to optimize sysctl.conf again? [y/n]")
        if loop  == "y":
          sysctl_commands()


        else:
            
              print("###############################################################################") 
              print("*                  warning: optimize sysctl.conf was failed                   *")
              print("###############################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without optimize sysctl.conf? [y/n]") == "n":
                exit ()

  sysctl_commands()


##############################################################################################################################
#****************************************************************************************************************************#
##############################################################################################################################


##############################
# install gnome-disk-utility #
##############################


  def disk_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'gnome-disk-utility', '-y'])
    print(pro.returncode)
    if int(pro.returncode)==0:
        print("##################################################")
        print("* gnome-disk-utility installation was successful *")
        print("##################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)
    else:
        print("#######################################################") 
        print("* warning: gnome-disk-utility installation was failed *")
        print("#######################################################")
        time.sleep(3)
        print("")
        print("##################################################################")
        print("Please check if the internet connection is available and try again")
        print("##################################################################")
        print("")
        loop = input("Do you want to try to install gnome-disk-utility again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          disk_commands()


        else:
            
              print("###############################################################################") 
              print("*             warning: Installing gnome-disk-utility was failed               *")
              print("###############################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without Installing gnome-disk-utility? [y/n]") == "n":
                exit ()


  disk_commands()


##############################################################################################################################
##############################################################################################################################


##################
# install nohang #
##################


  def nohang_commands():
    pro = subprocess.run(['sudo', 'add-apt-repository', 'ppa:oibaf/test', '-yy'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'update',])
    pro3 = subprocess.run(['sudo', 'apt-get', 'install', 'nohang', '-y'])
    pro4 = subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'nohang-desktop.service'])
    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode)==0:
        print("##################################################")
        print("*       nohang installation was successful       *")
        print("##################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)
    else:
        print("#######################################################") 
        print("*       warning: nohang installation was failed       *")
        print("#######################################################")
        time.sleep(3)
        print("")
        print("##################################################################")
        print("Please check if the internet connection is available and try again")
        print("##################################################################")
        print("")
        loop = input("Do you want to try to install htop nohang? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          nohang_commands()


        else:
            
              print("###############################################################################") 
              print("*                    warning: Installing nohang was failed                    *")
              print("###############################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without Installing nohang? [y/n]") == "n":
                exit ()


  nohang_commands()


##############################################################################################################################
##############################################################################################################################


#############################
#  Installation fish shell  #
#############################


  def fish_commands():
    pro = subprocess.run(['sudo', 'apt-add-repository', 'ppa:fish-shell/release-3', '-yy'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'update'])
    pro3 = subprocess.run(['sudo', 'apt-get', 'install', 'fish', '-y'])

    print(pro.returncode)
    print(pro.returncode)
    print(pro3.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode)==0:
       print("##########################################################") 
       print("*         Installation fish shell was successful         *")
       print("** fish is a smart and user-friendly command line shell **")
       print("##########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("##############################################################################") 
       print("*                warning: Installation fish shell was failed                 *")
       print("##############################################################################")
       time.sleep(3)
       print("")
       print("")
       loop = input("Do you want to try to install fish shell again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
        fish_commands()
            

  fish_commands() 


##############################################################################################################################
##############################################################################################################################


################################
# Installation grub-customizer #
################################


  def customizer_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'grub-customizer', '-y'])

    print(pro.returncode)

    if int(pro.returncode)==0:
        print("#########################################################") 
        print("*      Installation grub-customizer was successful      *")
        print("#########################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("############################################################################") 
        print("*             warning: Installation grub-customizer was failed             *")
        print("############################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to installing grub-customizer again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          customizer_commands()


        else:

                print("###############################################################################") 
                print("*                warning: installing grub-customizer was failed               *")
                print("###############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without installing grub-customizer? [y/n]") == "n":
                  exit ()

  customizer_commands()


##############################################################################################################################
##############################################################################################################################


############################
# Optimize and update grub #
############################


  def grub_commands():
    pro = subprocess.run(['sudo', 'cp', 'config-files/grub', '/etc/default/'])
    pro1 = subprocess.run(['sudo', 'update-grub'])
    print(pro.returncode)
    print(pro1.returncode)

    if int(pro.returncode + pro1.returncode)==0:
        print("#######################################################")
        print("*       optimize and update grub was successful       *")
        print("#######################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)
    else:
        print("############################################################") 
        print("*       warning: optimize and update grub was failed       *")
        print("############################################################")
        print("")
        print("")
        print("################################################################################")
        print("Some of the software you install later will not work related without this change")
        print("################################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to optimize and update grub again? [y/n]")  
        if loop  == "y":
          grub_commands()


        else:

                print("################################################################################") 
                print("*                 warning: optimize and update grub was failed                 *")
                print("################################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without optimize and update grub? [y/n]") == "n":
                  exit ()
            

  grub_commands()
  

##############################################################################################################################
##############################################################################################################################


#############################
# Update and optimize zswap #
#############################


  def zswap_commands():
    pro = subprocess.run(['sudo', 'cp', 'config-files/modules', '/etc/initramfs-tools/modules'])
    pro1 = subprocess.run(['sudo', 'update-initramfs', '-u'])

    print(pro.returncode)
    print(pro1.returncode)  


    if int(pro.returncode + pro1.returncode)==0:
        print("#######################################################")
        print("*      Update and optimize zswap was successful       *")
        print("#######################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)
    else:
        print("#############################################################") 
        print("*       warning: update and optimize zswap was failed       *")
        print("#############################################################")
        print("")
        print("")
        print("################################################################################")
        print("           System performance may decrease without this change                  ")
        print("################################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to update and optimize zswap? [y/n]")  
        if loop  == "y":
          zswap_commands()


        else:

                print("###############################################################################") 
                print("*               warning: update and optimize zswap was failed                 *")
                print("###############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without Installing optimize zswap? [y/n]") == "n":
                  exit ()


  zswap_commands()


##############################################################################################################################
##############################################################################################################################


##################################
#  Optimizing and improving SSD  #
##################################


  def trim_commands():
    pro = subprocess.run(['sudo', 'cp', 'config-files/trim', '/etc/cron.daily/'])
    pro2 = subprocess.run(['sudo', 'chmod', 'a+x', '/etc/cron.daily/trim'])

    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("#########################################################") 
        print("*      Optimizing and improving SSD was successful      *")
        print("#########################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("##############################################################################") 
        print("*              warning: optimizing and improving SSD was failed              *")
        print("##############################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to optimizing and improving SSD again? [y/n]")  
        if loop  == "y":
          trim_commands()


        else:

                print("###############################################################################") 
                print("*              warning: optimizing and improving SSD was failed               *")
                print("###############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without improving SSD? [y/n]") == "n":
                  exit ()

  trim_commands()

##############################################################################################################################
##############################################################################################################################


#############################
#   installing mesa-utils   #
#############################


  def mesa_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'mesa-utils'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'install', 'mesa-utils-extra', '-y'])

    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("############################################################") 
        print("*           installing mesa-utils was successful           *")
        print("############################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("###################################################################################") 
        print("*                   warning: installing mesa-utils was failed                     *")
        print("###################################################################################")
        time.sleep(3)
        print("")
        print("##################################################################")
        print("Please check if the internet connection is available and try again")
        print("##################################################################")
        print("")
        loop = input("Do you want to try to install mesa-utils again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          mesa_commands()


        else:
            
              print("###############################################################################") 
              print("*                  warning: Installing mesa-utils was failed                  *")
              print("###############################################################################")
              time.sleep(3)
              print("")
        
              while input("Do you want to continue without Installing mesa-utils? [y/n]") == "n":
              
                exit ()

  mesa_commands()


##############################################################################################################################
##############################################################################################################################


###############################
#   enable disk write cache   #
###############################


  def write_commands():
   pro = subprocess.run(['sudo', 'apt-get', 'install', 'hdparm'])
   pro2 = subprocess.run(['sudo', 'cp', 'config-files/hdparm.conf', '/etc/hdparm.conf'])

   print(pro.returncode)
   print(pro2.returncode)

   if int(pro.returncode + pro2.returncode)==0:
    print("###########################################################") 
    print("*         enable disk write cache  was successful         *")
    print("###########################################################")
    print("")
    print("the program will continue the installation process in a few seconds, please wait ...")
    time.sleep(3)

   else:

    print("##############################################################################") 
    print("*                warning: enable disk write cache was failed                 *")
    print("##############################################################################")
    time.sleep(3)
    print("")
    loop = input("Do you want to try to enable disk write cache again? [y/n]")  
    if loop  == "y":
      subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
      write_commands()


    else:

             print("###############################################################################") 
             print("*                 warning: enable disk write cache was failed                 *")
             print("###############################################################################")
             time.sleep(3)
             print("")
      
             while input("Do you want to continue without Installing htop? [y/n]") == "n":
              exit ()
            
  write_commands()


##############################################################################################################################
##############################################################################################################################


################################
#       Installing htop        #
################################


  def htop_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'htop'])

    print(pro.returncode)
 
    if int(pro.returncode)==0:
       print("###########################################################") 
       print("*             Installing htop was successful              *")
       print("###########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("##############################################################################") 
       print("*                   warning: Installing htop was failed                      *")
       print("##############################################################################")
       time.sleep(3)
       print("")
       print("##################################################################")
       print("Please check if the internet connection is available and try again")
       print("##################################################################")
       print("")
       loop = input("Do you want to try to install htop again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        htop_commands()


       else:
           
             print("################################################################################") 
             print("*                     warning: Installing htop was failed                      *")
             print("################################################################################")
             time.sleep(3)
             print("")
      
             while input("Do you want to continue without Installing htop? [y/n]") == "n":
              exit ()
            

  htop_commands()  


##############################################################################################################################
##############################################################################################################################


################################
# Installing indicator-cpufreq #
################################


  def indicator_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'indicator-cpufreq', '-y'])

    print(pro.returncode)
 
    if int(pro.returncode)==0:
       print("###########################################################") 
       print("*       Installing indicator-cpufreq was successful       *")
       print("###########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("##############################################################################") 
       print("*              warning: Installing indicator-cpufreq was failed              *")
       print("##############################################################################")
       time.sleep(3)
       print("")
       print("##################################################################")
       print("Please check if the internet connection is available and try again")
       print("##################################################################")
       print("")
       loop = input("Do you want to try to install indicator-cpufreq again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
        indicator_commands()


       else:
           
             print("##############################################################################") 
             print("*              warning: Installing indicator-cpufreq was failed              *")
             print("##############################################################################")
             time.sleep(3)
             print("")
      
             while input("Do you want to continue without Installing indicator-cpufreq? [y/n]") == "n":
              exit ()
            

  indicator_commands()

##############################################################################################################################
##############################################################################################################################


################################################
# Remove ubuntu reports and popularity-contest #
################################################


  def remove_re_commands():
    print("")
    print("remove ubuntu reports and popularity-contest ? ")
    print("")
    print("These tools help Ubuntu developers get anonymous information(according to ubuntu developers)")
    print("about system usage and bug fixes to improve distribution usage and create necessary updates.")
    print("The use of these tools depends on your choice.")
    print("")
    time.sleep(3)
    remove = input("Are you interested to remove ubuntu reports and popularity-contest? [y/n]")  
    if remove  == "y":

        pro = subprocess.run(['sudo', 'apt-get', 'remove', 'ubuntu-report', 'popularity-contest', 'apport', 'whoopsie', '-y'])
        pro2 = subprocess.run(['sudo', 'apt-get', 'purge', 'ubuntu-report', 'popularity-contest', 'apport', 'whoopsie', '-y'])

        print(pro.returncode)
        print(pro2.returncode)

        if int(pro.returncode + pro2.returncode)==0:
          print("#############################################################") 
          print("*remove ubuntu reports and popularity-contest was successful*")
          print("#############################################################")
          print("")
          print("the program will continue the installation process in a few seconds, please wait ...")  
          time.sleep(3)
        else:

          print("##############################################################################") 
          print("*      warning: remove ubuntu reports and popularity-contest was failed      *")
          print("##############################################################################")
          time.sleep(3)
          print("")
          loop = input("Do you want to try to remove ubuntu reports and popularity-contest again? [y/n]")  
          if loop  == "y":
           subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
           remove_re_commands() 


          else:
           
             print("##############################################################################") 
             print("*        warning: remove ubuntu reports and popularity-contest failed        *")
             print("##############################################################################")
             time.sleep(3)
             print("")
      

  remove_re_commands()  


##############################################################################################################################
##############################################################################################################################


##################################
# Installing profile-sync-daemon #
##################################

  def profile_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'profile-sync-daemon', '-y'])
    pro2 = subprocess.run(['sudo', 'cp', 'config-files/psd.conf', '/usr/share/psd/psd.conf'])

    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
      print("############################################################") 
      print("*       Installing profile-sync-daemon was successful      *")
      print("############################################################")
      print("")
      print("the program will continue the installation process in a few seconds, please wait ...")
      time.sleep(3)

    else:

      print("##############################################################################") 
      print("*             warning: installing profile-sync-daemon was failed             *")
      print("##############################################################################")
      time.sleep(3)
      print("")
      print("##################################################################")
      print("Please check if the internet connection is available and try again")
      print("##################################################################")
      print("")
      loop = input("Do you want to try to install profile-sync-daemon again? [y/n]")  
      if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        profile_commands()


      else:
          
            print("##############################################################################") 
            print("*             warning: installing profile-sync-daemon was failed             *")
            print("##############################################################################")
            time.sleep(3)
            print("")
    
            while input("Do you want to continue without installing profile-sync-daemon ? [y/n]") == "n":
             exit ()
          
  profile_commands()  


##############################################################################################################################
##############################################################################################################################


###############################
#    Installing irqbalance    #
###############################


  def irqbalance_commmands():
   pro = subprocess.run(['sudo', 'apt-get', 'install', '-y', 'irqbalance'])

   print(pro.returncode)

   if int(pro.returncode)==0:
      print("##########################################################") 
      print("*          Installing irqbalance was successful          *")
      print("##########################################################")
      print("")
      print("the program will continue the installation process in a few seconds, please wait ...")
      time.sleep(3)

   else:

      print("##############################################################################") 
      print("*                 warning: installing irqbalance was failed                  *")
      print("##############################################################################")
      time.sleep(3)
      print("")
      loop = input("Do you want to try to install irqbalance again? [y/n]")  
      if loop  == "y":
       subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
       irqbalance_commmands()


      else:

               print("##############################################################################") 
               print("*                  warning: install irqbalance was failed                    *")
               print("##############################################################################")
               time.sleep(3)
               print("")
         
               while input("Do you want to continue without Installing irqbalance? [y/n]") == "n":
                exit ()
              

  irqbalance_commmands()

##############################################################################################################################
##############################################################################################################################


###########################
#   Installing thermald   #
###########################


  def thermald_commmands():
   pro = subprocess.run(['sudo', 'apt-get', 'install', 'thermald'])

   print(pro.returncode)

   if int(pro.returncode)==0:
      print("#########################################################") 
      print("*          Installing thermald was successful           *")
      print("#########################################################")
      print("")
      print("the program will continue the installation process in a few seconds, please wait ...")
      time.sleep(3)

   else:

      print("##############################################################################") 
      print("*                  warning: installing thermald was failed                  *")
      print("##############################################################################")
      time.sleep(3)
      print("")
      loop = input("Do you want to try to install thermald again? [y/n]")  
      if loop  == "y":
       subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
       thermald_commmands()


      else:

               print("#############################################################################") 
               print("*                   warning: install thermald was failed                    *")
               print("#############################################################################")
               time.sleep(3)
               print("")
         
               while input("Do you want to continue without Installing thermald? [y/n]") == "n":
                exit ()
            
    
  thermald_commmands()


##############################################################################################################################
##############################################################################################################################


#############################
#    Installing fakeroot    #
#############################


  def fakeroot_commmands():
   pro = subprocess.run(['sudo', 'apt', 'install', 'fakeroot', '-y'])

   print(pro.returncode)

   if int(pro.returncode)==0:
      print("##########################################################") 
      print("*           Installing fakeroot was successful           *")
      print("##########################################################")
      print("")
      print("the program will continue the installation process in a few seconds, please wait ...")
      time.sleep(3)

   else:

      print("##############################################################################") 
      print("*                  warning: installing fakeroot was failed                   *")
      print("##############################################################################")
      time.sleep(3)
      print("")
      loop = input("Do you want to try to install fakeroot again? [y/n]")  
      if loop  == "y":
       subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
       fakeroot_commmands()


      else:

               print("#############################################################################") 
               print("*                   warning: install fakeroot was failed                    *")
               print("#############################################################################")
               time.sleep(3)
               print("")
         
               while input("Do you want to continue without Installing fakeroot? [y/n]") == "n":
                exit ()
            

  fakeroot_commmands()


##############################################################################################################################
##############################################################################################################################


###########################
#   Installing prelockd   #
###########################

  def perlockd_commands():
    pro = subprocess.run(['unzip', '-o', 'dependency/prelockd-master'])
    pro2 = subprocess.run(['sudo', 'bash', 'scripts/perlockd_install.sh'])

    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("#################################################") 
        print("*       Installing perlockd was successful      *")
        print("#################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("############################################################################") 
        print("*                 warning: installing perlockd was failed                  *")
        print("############################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to installing perlockd again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          perlockd_commands()


        else:

                print("###############################################################################") 
                print("*                  warning: installing perlockd was failed                    *")
                print("###############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without installing perlockd? [y/n]") == "n":
                  exit ()


  perlockd_commands()


##############################################################################################################################
##############################################################################################################################


###########################
# Installing lxde-desktop #
###########################


  def lxde_commands():
    print("")
    print("for very weak computers I recommend installing lxde-desktop")
    print("and after the installation is done login to lxde and consider removing")
    print("the previous desktop.")
    print("")
    print("Note !")
    print("If you have 2gb ram or more in the system")
    print("you do not have to perform this part")
    print("")
    time.sleep(1)

    lxde = input("Do you want to install lxde-desktop? [y/n] ")  
    if lxde  == "y":
      
      def lxdein_commands():
        
       pro = subprocess.run(['sudo', 'apt-get', 'install', 'lxde', '-y'])

       print(pro.returncode)

       if int(pro.returncode)==0:
          print("#############################################################") 
          print("*          Installing lxde-desktop was successful           *")
          print("#############################################################")
          print("")
          print("the program will continue the installation process in a few seconds, please wait ...")  
          time.sleep(3)

       else:

          print("#############################################################################") 
          print("*                warning: Installing lxde-desktop was failed                *")
          print("#############################################################################")
          time.sleep(3)
          print("")
          loop = input("Do you want to try to Installing lxde-desktop again ? [y/n]")  
          if loop  == "y":
           subprocess.run(['sudo', 'bash', 'scripts/fix.sh']) 
           lxdein_commands() 


          else:
           
             print("##############################################################################") 
             print("*                 warning: Installing lxde-desktop was failed                *")
             print("##############################################################################")
             time.sleep(3)
             print("")
      

      lxdein_commands()  


##### To improve performance on systems with very small resources the program will remove unnecessary packages 

      def unpa_commands():
        pro = subprocess.run(['sudo', 'rm', '-rf', '/var/cache/snapd/'])
        pro2 = subprocess.run(['sudo', 'apt-get', 'autoremove', '--purge', 'snapd', 'gnome-software-plugin-snap', '-y'])
        pro3 = subprocess.run("rm -fr ~/snap" ,shell=True)
        pro4 = subprocess.run(['sudo', 'apt-get', 'remove', 'bluez', '-y'])
        pro5 = subprocess.run(['sudo', 'apt-get', 'purge', 'bluez', '-y'])
        pro6 = subprocess.run(['sudo', 'apt-get', 'remove', 'xscreensaver', '-y'])
        pro7 = subprocess.run(['sudo', 'apt-get', 'purge', 'xscreensaver', '-y'])
        pro8 = subprocess.run(['sudo', 'apt-get', 'remove', 'clipit', '-y'])
        pro9 = subprocess.run(['sudo', 'apt-get', 'purge', 'clipit', '-y'])

        print(pro.returncode)
        print(pro2.returncode)
        print(pro3.returncode)
        print(pro4.returncode)
        print(pro5.returncode)
        print(pro6.returncode)
        print(pro7.returncode)
        print(pro8.returncode)
        print(pro9.returncode)

        if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode +
           pro7.returncode + pro8.returncode + pro9.returncode)==0:
          print("##########################################################") 
          print("*       remove unnecessary packages was successful       *")
          print("##########################################################")
          print("")
          print("the program will continue the installation process in a few seconds, please wait ...")
          time.sleep(3)

        else:

          print("##############################################################################") 
          print("*               warning: remove unnecessary packages was failed              *")
          print("##############################################################################")
          time.sleep(3)
          print("")
          print("")
          loop = input("Do you want to try to removing unnecessary packages again ? [y/n]")  
          if loop  == "y":
            subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
            unpa_commands()

      unpa_commands()

  lxde_commands()    


##############################################################################################################################
##############################################################################################################################


##############################
# Removing unnecessary tools #
##############################


  def unnecessary_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'remove', 'update-notifier', '-y'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'purge', 'update-notifier', '-y'])
    pro3 = subprocess.run(['sudo', 'apt-get', 'remove', 'thunderbird', '-y'])
    pro4 = subprocess.run(['sudo', 'apt-get', 'purge', 'thunderbird', '-y'])
    pro5 = subprocess.run(['sudo', 'apt-get', 'remove', 'gnome-software', '-y'])
    pro6 = subprocess.run(['sudo', 'apt-get', 'purge', 'gnome-software', '-y'])

    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro6.returncode)

 
    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode + pro6.returncode)==0:
       print("###########################################################") 
       print("*        removing unnecessary tools was successful        *")
       print("###########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("#############################################################################") 
       print("*              warning: removing unnecessary tools was failed               *")
       print("#############################################################################")
       time.sleep(3)
            

  unnecessary_commands()  


##############################################################################################################################
##############################################################################################################################


###############################
#     Installing synaptic     #
###############################


  def synaptic_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'synaptic', '-y'])

    print(pro.returncode)
 
    if int(pro.returncode)==0:
       print("###########################################################") 
       print("*           installing synaptic was successful            *")
       print("###########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("############################################################################") 
       print("*                 warning: installing synaptic was failed                  *")
       print("############################################################################")
       time.sleep(3)
       print("")
       print("##################################################################")
       print("Please check if the internet connection is available and try again")
       print("##################################################################")
       print("")
       loop = input("Do you want to try to install synaptic again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        synaptic_commands()


       else:
           
             print("###############################################################################") 
             print("*                   warning: installing synaptic was failed                   *")
             print("###############################################################################")
             time.sleep(3)
             print("")
      
             while input("Do you want to continue without installing synaptic? [y/n]") == "n":
              exit ()
            

  synaptic_commands()  


##############################################################################################################################
##############################################################################################################################


#######################
#    Repeat update    #
#######################


  def ru_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'update'])
    pro2 =subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'])

    print(pro.returncode)
    print(pro2.returncode)
 
    if int(pro.returncode + pro2.returncode)==0:
       print("###########################################################") 
       print("*              repeat update was successful               *")
       print("###########################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("##############################################################################") 
       print("*                     warning: repeat update was failed                      *")
       print("##############################################################################")
       time.sleep(3)
       print("")
       print("##################################################################")
       print("Please check if the internet connection is available and try again")
       print("##################################################################")
       print("")
       loop = input("Do you want to try to repeat update again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        ru_commands()


       else:
           
             print("###############################################################################") 
             print("*                     warning: repeat update was failed                       *")
             print("###############################################################################")
             time.sleep(3)
             print("")

            
  ru_commands()  


##############################################################################################################################
##############################################################################################################################


#############################################
# Installation and optimization zram-config #
#############################################


  def zram_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'zram-config'])
    pro2 = subprocess.run(['sudo', 'cp', 'config-files/init-zram-swapping', '/bin/init-zram-swapping'])

    print(pro.returncode)
    print(pro2.returncode)
 
    if int(pro.returncode + pro2.returncode)==0:
       print("############################################################") 
       print("* Installation and optimization zram-config was successful *")
       print("############################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("##############################################################################") 
       print("*       warning: Installation and optimization zram-config was failed        *")
       print("##############################################################################")
       time.sleep(3)
       print("")
       print("##################################################################")
       print("Please check if the internet connection is available and try again")
       print("##################################################################")
       print("")
       loop = input("Do you want to try to install zram-config again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        zram_commands()


       else:
           
             print("###############################################################################") 
             print("*         warning: Installing and optimization zram-config was failed         *")
             print("###############################################################################")
             time.sleep(3)
             print("")
      
             while input("Do you want to continue without Installing && optimization zram-config ? [y/n]") == "n":
              exit ()


  zram_commands()


##############################################################################################################################
##############################################################################################################################


##############################################
#   Installation && optimization tlp/tlpui   #
##############################################


  def tlp_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'tlp', '-y'])
    pro2 = subprocess.run(['sudo', 'systemctl', 'enable', 'tlp.service'])
    pro3 = subprocess.run(['sudo', 'systemctl', 'mask', 'systemd-rfkill.service'])
    pro4 = subprocess.run(['sudo', 'systemctl', 'mask', 'systemd-rfkill.socket'])
    pro5 = subprocess.run(['sudo', 'apt-get', 'install', 'python3-gi', 'python3-setuptools', 'python3-stdeb', 'dh-python', 'python-all', '-y'])
    pro6 = subprocess.run(['unzip', '-o', 'dependency/TLPUI'])
    pro7 = subprocess.run(['sudo', 'bash', 'scripts/tlpui_install.sh'])
    pro8 = subprocess.run(['sudo', 'cp', 'config-files/tlp.conf', '/etc/tlp.conf'])


    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)
    print(pro5.returncode)
    print(pro6.returncode)
    print(pro7.returncode)
    print(pro8.returncode)
 
    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode + pro5.returncode
     + pro6.returncode + pro7.returncode + pro8.returncode)==0:

       print("############################################################") 
       print("*     Installation and optimization tlp was successful     *")
       print("############################################################")
       print("")
       print("the program will continue the installation process in a few seconds, please wait ...")
       time.sleep(3)

    else:

       print("#############################################################################") 
       print("*          warning: Installation and optimization tlp was failed            *")
       print("#############################################################################")
       time.sleep(3)
       print("")
       print("##################################################################")
       print("Please check if the internet connection is available and try again")
       print("##################################################################")
       print("")
       loop = input("Do you want to try to install tlp again? [y/n]")  
       if loop  == "y":
        subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
        tlp_commands()


       else:
           
             print("##############################################################################") 
             print("*            warning: Installing and optimization tlp was failed             *")
             print("##############################################################################")
             time.sleep(3)
             print("")
      
             while input("Do you want to continue without Installing && optimization tlp ? [y/n]") == "n":
              exit ()   

  tlp_commands()  
  

##############################################################################################################################
##############################################################################################################################


##############################
#  Optimizing I/O scheduler  #
##############################


  def ioscheduler_commands():
    pro = subprocess.run(['sudo', 'cp', 'config-files/60-ioschedulers.rules', '/etc/udev/rules.d/'])
    pro2 = subprocess.run(['udevadm', 'control', '--reload'])

    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("########################################################") 
        print("*       Optimizing I/O scheduler was successful        *")
        print("########################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("##########################################################################") 
        print("*              warning: optimizing I/O scheduler was failed              *")
        print("##########################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to optimizing I/O scheduler again? [y/n]")  
        if loop  == "y":
          ioscheduler_commands()


        else:

                print("###########################################################################") 
                print("*              warning: optimizing I/O scheduler was failed               *")
                print("###########################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without optimizing I/O scheduler ? [y/n]") == "n":
                  exit ()


  ioscheduler_commands()


##############################################################################################################################
##############################################################################################################################


#########################################
# Installation && improvement memavaild #
#########################################

  def memavaild_commands():
    pro = subprocess.run(['unzip', '-o', 'dependency/memavaild-master'])
    pro2 = subprocess.run(['sudo', 'bash', 'scripts/memavaild_install.sh'])

    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("#########################################################") 
        print("*  Installation && improvement memavaild was successful *")
        print("#########################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("############################################################################") 
        print("*         warning: Installation && improvement memavaild was failed        *")
        print("############################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to installing memavaild again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          memavaild_commands()


        else:

                print("###############################################################################") 
                print("*                   warning: installing memavaild was failed                  *")
                print("###############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without installing memavaild? [y/n]") == "n":
                  exit ()

  memavaild_commands()


##############################################################################################################################
##############################################################################################################################


########################
# Installing tuned-adm #
########################

  def tuned_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'tuned', 'tuned-utils', 'tuned-utils-systemtap', '-y'])
    pro2 = subprocess.run(['sudo', 'tuned-adm', 'profile', 'desktop'])
    pro3 = subprocess.run(['sudo', 'tuned-adm', 'active',])


    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode)==0:
        print("#########################################################") 
        print("*          Installing tuned-adm was successful          *")
        print("#########################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("############################################################################") 
        print("*                 warning: Installing tuned-adm was failed                 *")
        print("############################################################################")
        time.sleep(3)
        print("")
        print("##################################################################")
        print("Please check if the internet connection is available and try again")
        print("##################################################################")
        print("")
        loop = input("Do you want to try to installing tuned-adm again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          tuned_commands()



        else:

                print("###############################################################################") 
                print("*                   warning: installing tuned-adm was failed                  *")
                print("###############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without installing tuned-adm ? [y/n]") == "n":
                  exit ()

  tuned_commands()

##############################################################################################################################
##############################################################################################################################


#######################
# Installing fail2ban #
#######################

  def fail2ban_commands():
    pro = subprocess.run(['sudo', 'apt-get', 'install', 'fail2ban', '-y'])
    pro2 = subprocess.run(['sudo', 'systemctl', 'enable', 'fail2ban'])
    pro3 = subprocess.run(['sudo', 'systemctl', 'start', 'fail2ban'])


    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode)==0:
        print("########################################################")
        print("*       Installing/enable fail2ban was successful      *")
        print("########################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("###########################################################################") 
        print("*                warning: Installing fail2ban was failed                 *")
        print("###########################################################################")
        time.sleep(3)
        print("")
        print("##################################################################")
        print("Please check if the internet connection is available and try again")
        print("##################################################################")
        print("")
        loop = input("Do you want to try to installing fail2ban again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          fail2ban_commands()


        else:

                print("###############################################################################") 
                print("*                   warning: installing fail2ban was failed                  *")
                print("###############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without installing fail2ban ? [y/n]") == "n":
                  exit ()

  fail2ban_commands()


##############################################################################################################################
##############################################################################################################################


##############################
# enable ufw && install gufw #
##############################

  def ufw_commands():
    pro = subprocess.run(['sudo', 'ufw', 'default', 'deny', 'incoming'])
    pro2 = subprocess.run(['sudo', 'ufw', 'default', 'allow', 'outgoing'])
    pro3 = subprocess.run(['sudo', 'ufw', 'enable'])
    pro4 = subprocess.run(['sudo', 'apt-get', 'install', 'gufw', '-y'])


    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)
    print(pro4.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode + pro4.returncode)==0:
        print("########################################################") 
        print("*               enable ufw was successful              *")
        print("########################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("###########################################################################") 
        print("*                   warning: install gufw was failed                      *")
        print("###########################################################################")
        time.sleep(3)
        print("")
        print("##################################################################")
        print("Please check if the internet connection is available and try again")
        print("##################################################################")
        print("")
        loop = input("Do you want to try to install gufw again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          ufw_commands()


        else:

                print("###############################################################################") 
                print("*                       warning: install gufw was failed                      *")
                print("###############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without install gufw ? [y/n]") == "n":
                  exit ()


  ufw_commands()


##############################################################################################################################
##############################################################################################################################


########################
# Installation ananicy #
########################

  def ananicy_commands():
    pro = subprocess.run(['sudo', 'bash', 'scripts/ananicy-install.sh'])
    pro2 = subprocess.run(['sudo', 'apt-get', '--fix-broken', 'install', '-y'])
    print(pro.returncode)
    print(pro2.returncode)

    if int(pro.returncode + pro2.returncode)==0:
        print("#######################################################") 
        print("*         Installation ananicy was successful         *")
        print("#######################################################")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("############################################################################") 
        print("*                warning: Installation ananicy was failed                  *")
        print("############################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to installing ananicy again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          ananicy_commands()


        else:

                print("##############################################################################") 
                print("*                   warning: installing ananicy was failed                   *")
                print("##############################################################################")
                time.sleep(3)
                print("")
          
                while input("Do you want to continue without installing ananicy? [y/n]") == "n":
                  exit ()

  ananicy_commands()


##############################################################################################################################
##############################################################################################################################


#######################
# Installing chromium #
#######################

  def chromium_commands():
    pro = subprocess.run(['sudo', 'add-apt-repository', 'ppa:system76/pop', '-yy'])
    pro2 = subprocess.run(['sudo', 'apt-get', 'update']) 
    pro3 = subprocess.run(['sudo', 'apt-get', 'install', 'chromium', '-y'])

    print(pro.returncode)
    print(pro2.returncode)
    print(pro3.returncode)

    if int(pro.returncode + pro2.returncode + pro3.returncode)==0:
        print("#########################################################") 
        print("*    Installing chromium(DEB version) was successful    *")
        print("#########################################################")
        print("")
        time.sleep(3)
        rmfirefox = input("Do you want to remove firefox-browser ? [y/n]")  
        if rmfirefox  == "y":
          subprocess.run(['sudo', 'apt-get', 'remove', 'firefox', '-y'])
          subprocess.run(['sudo', 'apt-get', 'purge', 'firefox', '-y'])
        print("")
        print("")
        print("the program will continue the installation process in a few seconds, please wait ...")
        time.sleep(3)

    else:

        print("###########################################################################") 
        print("*                 warning: Installing chromium was failed                 *")
        print("###########################################################################")
        time.sleep(3)
        print("")
        loop = input("Do you want to try to installing chromium again? [y/n]")  
        if loop  == "y":
          subprocess.run(['sudo', 'bash', 'scripts/fix.sh'])
          chromium_commands()


        else:

                print("###############################################################################") 
                print("*                  warning: installing chromium was failed                    *")
                print("###############################################################################")
                time.sleep(3)
                print("")

  chromium_commands()


##############################################################################################################################
##############################################################################################################################


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


##############################################################################################################################
##############################################################################################################################

aos_liquorix_commands()

print("")
print("For more details")
print("#########################################")
print("https://github.com/ramner98/LINUX-AOS.git")
print("#########################################")
time.sleep(3)
print("")
