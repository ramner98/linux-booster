#!/bin/bash

sudo -i sed -i 's/^GRUB_CMDLINE_LINUX_DEFAULT.*/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash zswap.enabled=1 zswap.compressor=lz4 zswap.max_pool_percent=25 zswap.zpool=z3fold systemd.unified_cgroup_hierarchy=1 apparmor=1 security=apparmor"/'  /etc/default/grub
