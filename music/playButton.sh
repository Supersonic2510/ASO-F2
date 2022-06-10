#!/bin/bash
echo "Content-type: text/html"
musicPath="/media/music"
commandFile="/musicCommands"
playlistFile="/playlist.txt"
PauseFlag="/PauseFlag"

read -r line < $musicPath$PauseFlag

if [[ $line != "Play" ]];then
	echo p > $musicPath$commandFile
	echo Play > $musicPath$PauseFlag
	logger -p local2.info "(pauseButton.sh) button is played"
fi
