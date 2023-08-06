#!/bin/bash -x

PATH=/opt/bin:/opt/sbin:/sbin:/bin:/usr/sbin:/usr/bin:/usr/syno/sbin:/usr/syno/bin:/usr/local/sbin:/usr/local/bin

mkdir -p /etc/sosbackups
mkdir -p /var/log/sosbackups

opkg update && opkg install ionice libmagic

CURDIR="$(dirname ${0})"

cp -a "${CURDIR}/init.d/sosbackups.sh" /usr/local/etc/rc.d/
cp -a "${CURDIR}/logrotate.d/sosbackups" /etc/logrotate.d/
cp -a "${CURDIR}/etc/sosbackups/sosbackups.yml.example" /etc/sosbackups/

if [ ! -f "/etc/sosbackups/exclude.lst" ];
then
    cp -a "${CURDIR}/etc/sosbackups/exclude.lst" /etc/sosbackups/
fi
