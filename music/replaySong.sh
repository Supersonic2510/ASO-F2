#!/bin/bash
musicPath="/media/music"
commandFile="/musicCommands"
playlistFile="/playlist.txt"
musicPlayer="/musicPlayer.sh"
CurrentSong="/CurrentSong"
PauseFlag="/PauseFlag"

read -r line < $musicPath$CurrentSong

if [[ -z $line ]]; then
	echo 1 > $musicPath$CurrentSong
	echo ll 1 $musicPath$playlistFile > $musicPath$commandFile
else
	number=$line
	
	echo $number > $musicPath$CurrentSong
	echo Play > $musicPath$PauseFlag
	echo ll $number $musicPath$playlistFile > $musicPath$commandFile
fi

read -r var < $musicPath$CurrentSong

logger -p local2.info "(replaySong.sh) replay song in position $var"
