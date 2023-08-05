#TODO: make it more safe.
if [ -z "$1" ]; then
    echo "Missinage Param"
    echo "Usage: certbotsafe <domain1,domain2>"
echo "Please DO NOT redirect html. becasue normal user cant reverse it."
certbot -n --apache --agree-tos -m --expand diepnh@magik.vn --domain "$1"