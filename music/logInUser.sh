#!/bin/bash
read -n "$CONTENT_LENGTH" QUERY_STRING_POST
saveIFS=$IFS
IFS='=&'
set -f
arrayKeys=($QUERY_STRING_POST)
IFS=$saveIFS

if [[ ${arrayKeys[0]} = username ]] && [[ ${arrayKeys[2]} = password ]];then
	  userLine=$(grep -n "${arrayKeys[1]}" ./userList.txt | cut -d: -f1)
	  passwordRead=$(sed -n ${userLine}p passwordList.txt)

	  if [[ $passwordRead = ${arrayKeys[3]} ]];then
	     sudo su ${arrayKeys[1]}
	     echo ${arrayKeys[1]} > ./loggedUser.txt
	     logger -p local2.info "(logInUser.sh) login user: {arrayKeys[1]}"
	  fi
fi
