#!/bin/bash
if [ -z "$1" ]; then
    echo "Missing parameters!"
    echo "Usage: sourcebackup <site>"
    exit
fi
site="$1"
log="/var/www/$site/log/source-backup.log"

cd /var/www/$site/html

#git branch backup
git config user.name "Opsbot"
git config user.email "opsbot@magik.vn"
git commit -am "Opsbot auto backup html" 
git push >> $log
