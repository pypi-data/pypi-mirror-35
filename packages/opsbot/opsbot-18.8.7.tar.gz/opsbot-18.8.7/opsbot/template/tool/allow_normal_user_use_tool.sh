echo "make this tool avaiable global"
mv {path} /usr/local/bin/{tool_command}
chown root:root /usr/local/bin/{tool_command} 
chmod o=rx,u+s /usr/local/bin/{tool_command}
