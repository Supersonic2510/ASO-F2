#!/bin/bash
read -n "$CONTENT_LENGTH" QUERY_STRING_POST
saveIFS=$IFS
IFS='=&'
set -f
arrayKeys=($QUERY_STRING_POST)
IFS=$saveIFS

if [[ ${arrayKeys[0]} = IPPosition ]] && [[ ${arrayKeys[2]} = IPSource ]] && [[ ${arrayKeys[4]} = IPDest ]] && [[ ${arrayKeys[6]} = IPProtocol ]] && [[ ${arrayKeys[8]} = IPPort ]] && [[ ${arrayKeys[10]} = type ]];then
	baseString="sudo iptables -R ${arrayKeys[13]} ${arrayKeys[1]}"
	if ! [[ -z ${arrayKeys[7]} ]];then
	baseString="${baseString} -p ${arrayKeys[7]}"
	fi
	if ! [[ -z ${arrayKeys[3]} ]];then
	baseString="${baseString} -s ${arrayKeys[3]}"
	fi
	if ! [[ -z ${arrayKeys[5]} ]];then
	baseString="${baseString} -d ${arrayKeys[5]}"
	fi
	if ! [[ -z ${arrayKeys[9]} ]];then
	baseString="${baseString} --dport ${arrayKeys[9]}"
	fi
	if ! [[ -z ${arrayKeys[11]} ]];then
	baseString="${baseString} -j ${arrayKeys[11]}"
	fi
	logger -p local2.info "(modifyIPTable.sh) modifying IP table: $baseString"
	eval $baseString
fi
