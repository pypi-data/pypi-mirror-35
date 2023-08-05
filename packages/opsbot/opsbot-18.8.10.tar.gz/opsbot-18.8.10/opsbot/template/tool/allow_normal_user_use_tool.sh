echo "make this tool avaiable global"
mv {path} /usr/local/bin/{tool_command}
echo "ALL ALL = NOPASSWD: /usr/local/bin/{tool_command}" > "/etc/sudoers.d/opsbot-allow-{tool_command}"
chmod 766 /usr/local/bin/{tool_command}

