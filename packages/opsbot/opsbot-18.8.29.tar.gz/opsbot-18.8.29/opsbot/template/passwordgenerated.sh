if [ -z "$1" ]; then
    echo "Usage: passwordgenerated.sh <password_variable>"
    exit
fi
touch configgenerated
source configgenerated
passwordvar=$1
passwordvarVal=${!passwordvar}
if [ -z $passwordvarVal ]; then
    echo "Password $passwordvar generated and store in configgenerated"
    passwordvarVal=$(openssl rand -base64 24)
    echo "$passwordvar=\"$passwordvarVal\""  >> configgenerated
fi