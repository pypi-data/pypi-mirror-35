echo "make virtual host config ..."
VHOST_PATH="/etc/apache2/sites-available/{site}.conf"
REDIRECT_CODE=""
if [ "{redirect_to_htmls}" == "1" ];
    then 
    REDIRECT_CODE="
    #REDIRECT HTTPS CODE HERE    "
fi

cat > $VHOST_PATH  <<EOL
<VirtualHost *:80>
    ServerName {site}
    DocumentRoot /var/www/{site}/{public_directory}
    <Directory /var/www/{site}/{public_directory}>
        AllowOverride All
    </Directory>
    ErrorLog  /var/www/{site}/error.log"
    CustomLog /var/www/{site}/access.log combined"
$REDIRECT_CODE
</VirtualHost>
EOL

echo "enable virtual host config ..."
a2ensite {site}