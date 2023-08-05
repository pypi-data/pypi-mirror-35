if [ -z "$2" ] ;  then
    echo "Missing Parameter."
    exit 1;
fi
SITE=$1
OWNER=$2
REDIRECT_TO_HTTPS=0
PUBLIC_DIRECTORY="html"
ACCESS_LOG=/var/www/$SITE/log/access-$SITE.log
ERROR_LOG=/var/www/$SITE/log/error-$SITE.log
DOMAINS="www.$SITE dev.$SITE" 

if [ $(whoami) != $OWNER ]; then
    echo "OWNER INVALID"
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
        -i=*|--include-domain=*)
        include_domains="${{i#*=}}"
        DOMAINS="$DOMAINS ${{include_domains//[,]/ }}"
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
echo "DOMAINS $DOMAINS"
echo "ACCESS_LOG $ACCESS_LOG"
echo "ERROR_LOG $ERROR_LOG"

if [ -d "/var/www/$SITE" ]; then
    echo "-----------------------------------"
    echo "SITE EXISTS. PLEASE CONTACT ADMIN"
    exit 1
fi

{script_site_rule}

{script_site_vhost}

{script_site_vhost_ssl}