if [ -z "$1" ]; then
    echo "Usage: passwordgenerated.sh <password_variable>"
    exit
fi
touch passwordgenerated.txt
source passwordgenerated.txt
passwordvar=$1
passwordvarVal=${!passwordvar}
if [ -z $passwordvarVal ]; then
    echo "genpassword $passwordvar"
    passwordvarVal=$(openssl rand -base64 24)
    echo "$passwordvar=\"$passwordvarVal\""  >> passwordgenerated.txt
fi