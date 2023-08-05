if [ -z "$1" ]; then
    echo "Usage: passwordgenerated.sh <password_variable>"
    exit
fi
touch configenerated
source configenerated
passwordvar=$1
passwordvarVal=${!passwordvar}
if [ -z $passwordvarVal ]; then
    echo "Password $passwordvar generated and store in configenerated"
    passwordvarVal=$(openssl rand -base64 24)
    echo "$passwordvar=\"$passwordvarVal\""  >> configenerated
fi