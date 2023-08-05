#TODO: make it more safe.
if [ -z "$1" ]; then
    echo "Missinage Param"
    echo "Usage: certbotsafe <domain1,domain2>"
fi

echo "Please DO NOT SELECT redirect to https. Because a normal user cant reverse this process."
certbot -n --apache --agree-tos --expand -m diepnh@magik.vn --domain "$1"