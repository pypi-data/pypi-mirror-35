#gen a ssh key
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
ssh-keygen -t rsa -b 4096 -C "$ADMIN_EMAIL" -N "" -f ~/.ssh/id_rsa

eval "$(ssh-agent -s)"

ssh-add ~/.ssh/id_rsa

