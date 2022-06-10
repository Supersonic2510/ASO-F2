#!/bin/bash
musicPath="/media/music"
commandFile="/musicCommands"
playlistFile="/playlist.txt"
musicPlayer="/musicPlayer.sh"
CurrentSong="/CurrentSong"
PauseFlag="/PauseFlag"

logger -p local2.info "(startPlaylist.sh) creating a new screen: musicPLayer"

screen -S musicPlayer -d -m bash $musicPath$musicPlayer

logger -p local2.info "(startPlaylist.sh) loading pLaylist ..."

sleep 1

echo "Loading playlist"
sudo chmod g+rwx $musicPath$commandFile
sudo chgrp mediagroup $musicPath$commandFile
echo ll -1 $musicPath$playlistFile > $musicPath$commandFile

logger -p local2.info "(startPlaylist.sh) loaded done"

echo 1 > $musicPath$CurrentSong
echo Pause > $musicPath$PauseFlag
