echo "create unix user ..."
encryptedPass=`openssl passwd -crypt "${username}_unix_password"`
#TODO: Fix warning.
useradd {username} -M -p $encryptedPass
