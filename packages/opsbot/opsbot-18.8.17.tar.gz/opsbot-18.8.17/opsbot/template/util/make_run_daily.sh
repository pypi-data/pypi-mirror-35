
echo "Make a daily cron"
cat <(crontab -l) <(echo "{minute} {hour} * * * /usr/bin/timeout -s 2 240 {command}") | crontab -