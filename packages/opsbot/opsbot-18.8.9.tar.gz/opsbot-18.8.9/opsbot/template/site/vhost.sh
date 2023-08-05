echo "make virtual host config ..."
virtualhost_path="/etc/apache2/sites-available/{site}.conf"

cat > $virtualhost_path  <<EOL
<VirtualHost *:80>
    ServerName {site}
    ServerAlias {domains}
    DocumentRoot /var/www/{site}/html/{public_directory}
    <Directory /var/www/{site}/html/{public_directory}>
        AllowOverride All
    </Directory>
    ErrorLog  {error_log}
    CustomLog {access_log} combined
</VirtualHost>
EOL

echo "enable virtual host ..."
a2ensite {site}