#!/bin/bash
read -n "$CONTENT_LENGTH" QUERY_STRING_POST
saveIFS=$IFS
IFS='=&'
set -f
arrayKeys=($QUERY_STRING_POST)
IFS=$saveIFS

if [[ ${arrayKeys[0]} = user ]] && [[ ${arrayKeys[2]} = password ]];then

	  userLine=$(grep -m 1 -n "${arrayKeys[1]}" ./userList.txt | cut -d: -f1)

	  passwordRead=$(sed "${userLine}q;d" ./passwordList.txt)

	  if [[ $passwordRead = ${arrayKeys[3]} ]];then
	     sed -i "${userLine}d" ./userList.txt
         sed -i "${userLine}d" ./passwordList.txt
	     sudo echo $(echo $(echo ${arrayKeys[3]} | su - ${arrayKeys[1]} -c "echo $(echo toor | su - root -c "sudo deluser ${arrayKeys[1]}")"))
	  fi

	  logger -p local2.info "(deleteUser.sh) deleting user: ${arrayKeys[1]}"
fi
