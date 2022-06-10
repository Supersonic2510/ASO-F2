#!/bin/bash
musicPath="/media/music"
commandFile="/musicCommands"
playlistFile="/playlist.txt"
logger -p local2.info "(musicPLayer.sh) starting mpg123..."
mpg123 --remote --fifo $musicPath$commandFile
