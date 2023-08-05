echo "create unix user ..."
encrypted=$(python -c "import crypt; print(crypt.crypt(\"${username}_unix_password\", \"Fx\"))")
useradd --create-home --password $encrypted {username}
chmod 700 "/home/{username}"