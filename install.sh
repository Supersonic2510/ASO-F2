#!/bin/bash
sudo bash ./ASO-F1/install.sh
sudo apt-get install apache2
sudo apt-get install sysstat
sudo groupadd mediagroup
sudo usermod -a -G mediagroup root
sudo usermod -a -G groupname $USER
sudo rm -rf /media/music
sudo cp -R ./music /media/music/
sudo rm -rf /etc/apache2/
sudo cp -R ./apache2 /etc/apache2/
sudo chgrp -R mediagroup /media/music/
sudo chmod -R 777 /media/music
sudo bash /media/music/startPlaylist.sh
