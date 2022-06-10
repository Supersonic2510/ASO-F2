#!/bin/bash
read -n "$CONTENT_LENGTH" QUERY_STRING_POST
saveIFS=$IFS
IFS='=&'
set -f
arrayKeys=($QUERY_STRING_POST)
IFS=$saveIFS

echo $(sudo crontab -u ${arrayKeys[13]} -l > mycron) 
	
	string="${arrayKeys[3]} ${arrayKeys[5]} ${arrayKeys[7]} ${arrayKeys[9]} ${arrayKeys[11]} ${arrayKeys[1]}"
	string=${string//[\*]/\\*}

	if ! [[ -z $string ]] ;then
		sed -i "/${string}/d" mycron
		sudo crontab -u ${arrayKeys[13]} mycron
		rm mycron

		logger -p local2.info "(removeCronTask.sh) removing cron ${string}"
	fi
	


