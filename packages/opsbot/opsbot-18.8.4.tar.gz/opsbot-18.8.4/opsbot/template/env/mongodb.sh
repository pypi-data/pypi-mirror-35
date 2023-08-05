echo "install mongodb ..."
apt install -y mongodb

echo "create root"
mongo admin --eval "db.createUser({user: \"root\", pwd: \"$root_mongodb_password\",roles:[\"root\"]});"

echo "fix auth = true"
echo "auth = true" >> /etc/mongodb.conf