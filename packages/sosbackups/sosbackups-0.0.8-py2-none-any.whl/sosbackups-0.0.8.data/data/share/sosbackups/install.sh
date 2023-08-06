#!/bin/bash -x

mkdir -p /etc/sosbackups
mkdir -p /var/log/sosbackups

opkg update && opkg install ionice libmagic

CURDIR="$(dirname ${0})"

cp -a "${CURDIR}/init.d/sosbackups.sh" /usr/local/etc/rc.d/
cp -a "${CURDIR}/logrotate.d/sosbackups" /etc/logrotate.d/
cp -a "${CURDIR}/etc/sosbackups/exclude.lst" /etc/sosbackups/
cp -a "${CURDIR}/etc/sosbackups/sosbackups.yml.example" /etc/sosbackups/
