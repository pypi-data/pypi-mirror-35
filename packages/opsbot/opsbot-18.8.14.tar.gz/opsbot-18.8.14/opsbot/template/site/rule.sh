echo "make directory for website ..."
mkdir /var/www/{site}

echo "make directory for html"
mkdir /var/www/{site}/html
chown {owner}:www-data /var/www/{site}/html
chmod g+s /var/www/{site}/html
chmod o-rwx /var/www/{site}/html

echo "chown -R {owner}:www-data /var/www/{site}/html" >  "/var/www/{site}/resetowner.sh"
chmod 755 "/var/www/{site}/resetowner.sh"
echo "{owner} ALL = NOPASSWD: /var/www/{site}/resetowner.sh" >> "/etc/sudoers.d/opsbot-owners"

echo "make log file for website ..."
mkdir /var/www/{site}/log
touch {access_log}
touch {error_log}

echo "config log rotate"
cat > "/etc/logrotate.d/vhost-{site}.lr" <<EOL
/var/www/{site}/log/*.log {{
        monthly
        missingok
        rotate 12
        maxsize 500M
        notifempty
        create 644 root adm
        sharedscripts
        postrotate
                if /etc/init.d/apache2 status > /dev/null ; then \
                    /etc/init.d/apache2 reload > /dev/null; \
                fi;
        endscript
        prerotate
                if [ -d /etc/logrotate.d/httpd-prerotate ]; then \
                        run-parts /etc/logrotate.d/httpd-prerotate; \
                fi; \
        endscript
}}
EOL



