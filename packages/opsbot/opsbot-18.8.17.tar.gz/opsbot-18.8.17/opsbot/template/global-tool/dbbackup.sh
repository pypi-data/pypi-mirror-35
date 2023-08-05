#!/bin/bash
if [ -z "$1" ]; then
    echo "Missing parameters!"
    echo "Usage: dbbackup <site>"
    exit
fi

site="$1"
log="/var/www/$site/log/db-backup.log"

/var/www/$site/tool/dbdump.sh >> $log

cd /var/www/$site/db
#git branch backup
git config user.name "Opsbot"
git config user.email "opsbot@magik.vn"
git commit -am "Opsbot auto backup database" >> $log
git push >> $log
