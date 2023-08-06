#!/bin/bash -x

mkdir -p /etc/sosbackups
mkdir -p /var/log/sosbackups

opkg update && opkg install ionice libmagic

CURDIR="(dirname ${0})"

cp -a "${CURDIR}/../../sosbackups/etc/init.d/sosbackups.sh" /usr/local/etc/rc.d/
cp -a "${CURDIR}/../../sosbackups/etc/logrotate.d/sosbackups" /etc/logrotate.d/
cp -a "${CURDIR}/../../sosbackups/etc/sosbackups/exclude.lst" /etc/sosbackups/
cp -a "${CURDIR}/../../sosbackups/etc/sosbackups/sosbackups.yml.example" /etc/sosbackups/
