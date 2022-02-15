#!/bin/bash

sudo -i sed -i 's/^GRUB_CMDLINE_LINUX_DEFAULT.*/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash apparmor=0 security=apparmor"/'  /etc/default/grub
