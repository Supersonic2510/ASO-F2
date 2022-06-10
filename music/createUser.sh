#!/bin/bash
read -n "$CONTENT_LENGTH" QUERY_STRING_POST
saveIFS=$IFS
IFS='=&'
set -f
arrayKeys=($QUERY_STRING_POST)
IFS=$saveIFS

if [[ ${arrayKeys[0]} = user ]] && [[ ${arrayKeys[2]} = password ]];then
	sudo useradd ${arrayKeys[1]}
	echo $(echo -e "${arrayKeys[3]}\n${arrayKeys[3]}" | sudo passwd ${arrayKeys[1]})
	sudo usermod -a -G mediagroup ${arrayKeys[1]}
	sudo usermod -a -G sudo ${arrayKeys[1]}
	echo ${arrayKeys[1]} >> ./userList.txt
	echo ${arrayKeys[3]} >> ./passwordList.txt
	logger -p local2.info "(createUser.sh) creating a new user: ${arrayKeys[1]}"
fi
