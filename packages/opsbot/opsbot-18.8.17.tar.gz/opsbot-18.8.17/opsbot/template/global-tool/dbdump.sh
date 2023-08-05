#!/bin/bash
if [ -z "$4" ]; then
    echo "Missing parameters!"
    echo "usage : dbdump <import|export> <site> <db_username> <db_password>"
    exit
fi

type="$1"
site="$2"
db_username="$3"
db_password="$4"

db_path="/var/www/$site/db"
lst_path="$db_path/dblist.opsbot"

CONNECT_STR="-u$db_username -p$db_password"
if [ ! -f $lst_path ]; then
    echo "db config not exists"
    exit;
fi

while IFS= read -r line || [ -n "$line" ];  do
    database=$line
    if [ "$line" = "" ]; then
        continue
    fi
    echo "Begin dump database[$line]"
    if [ "$type" = "export" ]; then
        mysqldump $CONNECT_STR --skip-dump-date --single-transaction $database > "$db_path/$database.sql"
    fi
    if [ "$type" = "import" ]; then
        mysqladmin $CONNECT_STR create namix_web
        mysql $CONNECT_STR $database <  "$db_path/$database.sql"
    fi
done < "$lst_path"