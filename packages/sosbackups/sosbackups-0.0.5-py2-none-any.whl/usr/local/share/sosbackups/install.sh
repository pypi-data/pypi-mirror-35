#!/bin/bash -x

mkdir -p /etc/sosbackups
mkdir -p /var/log/sosbackups

opkg update && opkg install ionice libmagic
