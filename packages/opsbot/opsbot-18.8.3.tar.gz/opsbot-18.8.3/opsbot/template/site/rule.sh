echo "make directory for website ..."
mkdir /var/www/{site}
chown -R {owner}:www-data /var/www/{site}
chmod g+s /var/www/{site}
chmod o-rwx /var/www/{site}

echo "make log file for website ..."
touch /var/www/{site}/access-{site}.log
touch /var/www/{site}/error-{site}.log
chmod g+w  /var/www/{site}/*.log