#!/bin/bash
read -n "$CONTENT_LENGTH" QUERY_STRING_POST
saveIFS=$IFS
IFS='=&'
set -f
arrayKeys=($QUERY_STRING_POST)
IFS=$saveIFS

if [[ ${arrayKeys[0]} = pid ]] && [[ ${arrayKeys[2]} = seconds ]];then
        pid=${arrayKeys[1]}
        seconds=${arrayKeys[3]}

	kill -STOP $pid

	logger -p local2.info "(interruptPID.sh) interrupting PID: $pid"

        sleep $seconds

        kill -CONT $pid

	logger -p local2.info "(interruptPID.sh) resuming PID: $pid"
fi
