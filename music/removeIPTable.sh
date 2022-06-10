#!/bin/bash
read -n "$CONTENT_LENGTH" QUERY_STRING_POST
saveIFS=$IFS
IFS='=&'
set -f
arrayKeys=($QUERY_STRING_POST)
IFS=$saveIFS

if [[ ${arrayKeys[0]} = IPPosition ]] && [[ ${arrayKeys[2]} = IPSource ]] && [[ ${arrayKeys[4]} = IPDest ]] && [[ ${arrayKeys[6]} = IPProtocol ]] && [[ ${arrayKeys[8]} = IPPort ]] && [[ ${arrayKeys[10]} = type ]];then
	sudo iptables -D ${arrayKeys[13]} ${arrayKeys[1]}
	logger -p local2.info "(removeIPTable.sh) removing IP table in position ${arrayKeys[1]}"
fi
