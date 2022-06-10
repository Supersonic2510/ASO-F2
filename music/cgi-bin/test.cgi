#!/bin/bash
numberLines=$(wc -l < /media/music/playlist.txt)

arrayLines=()

readarray -t arrayLines < /media/music/playlist.txt

echo "Content-type: text/html"
echo '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Music Player</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">

    <style>
        .playButton{
            font-size: 50px;
            cursor: pointer;
        }
	.playList{
            font-size: 24px;
            display: block;
            text-align: center;
            gap: 12px
        }
        #play-pause-div{
            display: flex;
            flex-direction: column;
            text-align: center;
            gap: 12px;
        }
        #player-controller{
            display: flex;
            flex-direction: row;
            align-self: center;
            gap: 12px;
        }

    </style>

    <ul>
        <li><a href="/music/cgi-bin/register.cgi">Register</a></li>
        <li><a href="/music/cgi-bin/server.cgi">Server</a></li>
        <li><a href="/music/cgi-bin/processManagement.cgi">Process Management</a></li>
        <li><a href="/music/cgi-bin/userManagement.cgi">User Management</a></li>
        <li><a href="/music/cgi-bin/monitoring.cgi">Monitoring</a></li>
        <li><a href="/music/cgi-bin/packetFiltering.cgi">Packet Filtering</a></li>
        <li><a href="/music/cgi-bin/schedulingManager.cgi">Scheduling Manager</a></li>
        <li><a href="/music/cgi-bin/logger.cgi">Logger</a></li>
    </ul>
</head>

<body>
<div id="play-pause-div">
    <h1>Music Player ver 0.1</h1>
    <div id="player-controller">
        <button id="previousButton" class="playButton"><</button>
        <button id="musicButton" class="playButton">
            <i class="fas fa-play"></i>
        </button>
        <button id="nextButton" class="playButton">></button>
    </div>
    <div>
        <button id="shuffleButton" class="playButton">Shuffle</button>

        <button id="replayButton" class="playButton">Replay</button>
    </div>
</div>

<div class="playList">
    <h1>PlayList</h1>
'

for (( c=0; c<$numberLines; c++ ))
do  
   var=$( echo ${arrayLines[$c]} | sed -r 's/\/media\/music\/song\///g' )
   printf '    <p>· %s</p>\n' "$var"
done

echo '
</div>

</body>
</html>
<script>
    var musicIsPlaying = false;
    var musicButton = document.getElementById("musicButton");
    musicButton.addEventListener("click", playPause);

    function playPause() {
        musicIsPlaying = !musicIsPlaying;
        if (musicIsPlaying) {
            musicButton.innerHTML = "<i class=\"fa-solid fa-pause\"></i>";
        }else  {
            musicButton.innerHTML = "<i class=\"fas fa-play\"></i>";
        }
    }

    //Jquerys
    $(document).ready(function(){
        $("#musicButton").click(function(){
            if (!musicIsPlaying) {
                $.post("/music/pauseButton.sh", null, null);
            } else {
                $.post("/music/playButton.sh", null, null);
            }
        });
        $("#previousButton").click(function (){
            musicButton.innerHTML = "<i class=\"fa-solid fa-pause\"></i>";
            musicIsPlaying = true;

            $.post("/music/previousSong.sh", null, null);
        });
        $("#nextButton").click(function (){
            musicButton.innerHTML = "<i class=\"fa-solid fa-pause\"></i>";
            musicIsPlaying = true;

            $.post("/music/nextSong.sh", null, null);
        });
        $("#shuffleButton").click(function () {
            $.post("/music/shuffleSong.sh", null, null);
            location.reload();
        });
        $("#replayButton").click(function () {
            $.post("/music/replaySong.sh", null, null);
        });
    });
</script>
'
