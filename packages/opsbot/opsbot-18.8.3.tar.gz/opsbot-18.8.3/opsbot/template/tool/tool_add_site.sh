if [ -z "$2" ] ;  then
    echo "Missing Parameter."
    exit 1;
fi
SITE=$1
OWNER=$2
REDIRECT_TO_HTTPS=0
PUBLIC_DIRECTORY="html"

if [ $(whoami) != $OWNER ]; then
    echo "OWNER INVALID"
    exit 1
fi

if [ -d "/var/www/$SITE" ]; then
    echo "SITE EXISTS. PLEASE CONTACT ADMIN"
    exit 1
fi

for i in "$@"
    do
    case $i in
        -r|--redirect-to-https)
        REDIRECT_TO_HTTPS=1
        shift
        ;;
        -p=*|--public-directory=*)
        PUBLIC_DIRECTORY="${{i#*=}}"
        shift
        ;;
        *)
              # unknown option
        ;;
    esac
    done
echo "SITE $SITE"
echo "OWNER $OWNER"
echo "REDIRECT_TO_HTTPS $REDIRECT_TO_HTTPS"
echo "PUBLIC_DIRECTORY $PUBLIC_DIRECTORY"

{script_site_rule}

{script_site_vhost}

{script_site_vhost_ssl}