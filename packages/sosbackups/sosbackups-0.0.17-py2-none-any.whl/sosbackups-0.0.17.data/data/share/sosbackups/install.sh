#!/bin/bash -x

PATH=/opt/bin:/opt/sbin:/sbin:/bin:/usr/sbin:/usr/bin:/usr/syno/sbin:/usr/syno/bin:/usr/local/sbin:/usr/local/bin

mkdir -p /etc/sosbackups
mkdir -p /var/log/sosbackups

IPKG_BIN="$(which ipkg)"
OPKG_BIN="$(which opkg)"

if [ ! -z "${OPKG_BIN}" ];
then
    ${OPKG_BIN} update && ${OPKG_BIN} install ionice libmagic
elif [ ! -z "${IPKG_BIN}" ];
then
    ${IPKG_BIN} update && ${IPKG_BIN} install file
fi

CURDIR="$(dirname ${0})"

cp -a "${CURDIR}/init.d/sosbackups.sh" /usr/local/etc/rc.d/
cp -a "${CURDIR}/logrotate.d/sosbackups" /etc/logrotate.d/
cp -a "${CURDIR}/etc/sosbackups/sosbackups.yml.example" /etc/sosbackups/

if [ ! -f "/etc/sosbackups/rc.default" ];
then
    cp -a "${CURDIR}/etc/sosbackups/rc.default" /etc/sosbackups/
fi

if [ ! -f "/etc/sosbackups/exclude.lst" ];
then
    cp -a "${CURDIR}/etc/sosbackups/exclude.lst" /etc/sosbackups/
fi
