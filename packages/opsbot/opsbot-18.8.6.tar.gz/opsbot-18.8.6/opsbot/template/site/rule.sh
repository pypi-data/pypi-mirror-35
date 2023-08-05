echo "make directory for website ..."
mkdir /var/www/{site}
chown -R {owner}:www-data /var/www/{site}
chmod g+s /var/www/{site}
chmod o-rwx /var/www/{site}

echo "make log file for website ..."
touch {access_log}
touch {error_log}
chmod g+w,o-rwx  {access_log}
chmod g+w,o-rwx  {error_log}