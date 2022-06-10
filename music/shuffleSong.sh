#!/bin/bash
numberLines=$(wc -l < /media/music/playlist.txt)

arrayLines=()

readarray -t arrayLines < /media/music/playlist.txt

logger -p local2.info "(shuffleSong.sh) list song shuffing..."

for (( c=0; c<$numberLines; c++ ))
do  
   if [ $c -gt 1 ]; then
        for (( i=0; i<($c - 1); i++ ))
        do  
           j=$(( $i + $(( $(($RANDOM)) / $(( $(( 32767 / ($(( $c - $i ))) )) + 1 )) )) ))
           
           
           echo ${arrayLines[$i]}
           echo ${arrayLines[$j]}
           
           t=${arrayLines[$j]}
           
           arrayLines[$j]=${arrayLines[$i]}
           
           arrayLines[$i]=$t
           
           echo ${arrayLines[$i]}
           echo ${arrayLines[$j]}
        done
   fi
done

f() { arrayLines=("${BASH_ARGV[@]}"); }

shopt -s extdebug
f "${arrayLines[@]}"
shopt -u extdebug


printf "%s\n" "${arrayLines[@]}" > /media/music/playlist.txt

logger -p local2.info "(shuffleSong.sh) list song shuffled"
