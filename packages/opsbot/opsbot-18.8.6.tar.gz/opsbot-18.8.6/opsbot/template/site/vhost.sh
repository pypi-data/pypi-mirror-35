echo "make virtual host config ..."
virtualhost_path="/etc/apache2/sites-available/{site}.conf"
redirect_to_htmls="{redirect_to_htmls}"

#TODO : write #redirect_code 
redirect_code=""
if [ "$redirect_to_htmls" == "1" ]; then 
    redirect_code="
"
fi

cat > $virtualhost_path  <<EOL
<VirtualHost *:80>
    ServerName {site}
    ServerAlias {domains}
    DocumentRoot /var/www/{site}/{public_directory}
    <Directory /var/www/{site}/{public_directory}>
        AllowOverride All
    </Directory>
    ErrorLog  {error_log}
    CustomLog {access_log} combined
$redirect_code
</VirtualHost>
EOL

echo "enable virtual host ..."
a2ensite {site}