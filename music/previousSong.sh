#!/bin/bash
musicPath="/media/music"
commandFile="/musicCommands"
playlistFile="/playlist.txt"
CurrentSong="/CurrentSong"
PauseFlag="/PauseFlag"

read -r line < $musicPath$CurrentSong

if [[ -z $line ]]; then
	echo 1 > $musicPath$CurrentSong
	echo ll 1 $musicPath$playlistFile > $musicPath$commandFile
else
	number=$((line - 1))
	
	if [[ $number -lt 1 ]]; then
		number=2
	fi
	
	echo $number > $musicPath$CurrentSong
	echo Play > $musicPath$PauseFlag
	echo ll $number $musicPath$playlistFile > $musicPath$commandFile
fi

read -r var $musicPath$CurrentSong

logger -p local2.info "(previousSong.sh) previous song in position $var"
