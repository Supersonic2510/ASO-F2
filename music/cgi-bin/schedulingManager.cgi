#!/bin/bash
echo "Content-type: text/html"
echo '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Packet Filtering</title>
    <ul>
        <li><a href="/music/cgi-bin/test.cgi">JuggerBox</a></li>
        <li><a href="/music/cgi-bin/register.cgi">Register</a></li>
        <li><a href="/music/cgi-bin/server.cgi">Server</a></li>
        <li><a href="/music/cgi-bin/processManagement.cgi">Process Management</a></li>
        <li><a href="/music/cgi-bin/userManagement.cgi">User Management</a></li>
        <li><a href="/music/cgi-bin/monitoring.cgi">Monitoring</a></li>
        <li><a href="/music/cgi-bin/packetFiltering.cgi">Packet Filtering</a></li>
        <li><a href="/music/cgi-bin/logger.cgi">Logger</a></li>
    </ul>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
'

userLogged=$(sed -n 1p /media/music/loggedUser.txt)

echo "<article>
    <h2>Cron Task User: $userLogged</h2>
" 

sudo crontab -u $userLogged -l | while read line;do
      echo "${line} <br>"

      done


echo "
</article>
<form>
    <h2>Task Manager:</h2>
    <label for="command">Command to perform:</label><br>
    <input type="text" id="command" name="command"><br>
    <label for="minute">Minute to perform:</label><br>
    <input type="number" id="minute" name="minute" min="0" max="59"><br>
    <label for="minute">Hour to perform:</label><br>
    <input type="number" id="hour" name="hour" min="0" max="23"><br>
    <label for="day">Day of the month to perform:</label><br>
    <input type="number" id="day" name="day" min="1" max="31"><br>
    Month to perform:<br>
    <select name="month" id="month">
        <option value="*" selected>Monthly</option>
        <option value="1">January</option>
        <option value="2">February</option>
        <option value="3">March</option>1
        <option value="4">April</option>
        <option value="5">May</option>
        <option value="6">June</option>
        <option value="7">July</option>
        <option value="8">August</option>
        <option value="9">September</option>
        <option value="10">October</option>
        <option value="11">November</option>
        <option value="12">December</option>
    </select><br>
    Day to perform:<br>
    <select name="weekDay" id="weekDay">
        <option value="*" selected>Daily</option>
        <option value="1">Monday</option>
        <option value="2">Tuesday</option>
        <option value="3">Wednesday</option>
        <option value="4">Thursday</option>
        <option value="5">Friday</option>
        <option value="6">Saturday</option>
        <option value="7">Sunday</option>
    </select><br>
    
    <input id="addTask" type="button" value="Add Task">
    <input id="deleteTask" type="button" value="Delete Task">

</form>
"

echo '
</body>
<script>
	function syncDelay(milliseconds){
        var start = new Date().getTime();
        var end=0;
        while( (end-start) < milliseconds){
            end = new Date().getTime();
        }
    }

    //Jquerys
    $(document).ready(function(){
        $("#addTask").click(function(){
            var command = document.getElementById("command").value;
            var minute = document.getElementById("minute").value;
            var hour = document.getElementById("hour").value;
            var day = document.getElementById("day").value;
            var month = document.getElementById("month").value;
            var weekDay= document.getElementById("weekDay").value;
            

            $.post("/music/addCronTask.sh", { command: command, minute: minute, hour: hour, day: day, month: month, weekDay: weekDay, userLogged: "'${userLogged}'"}, null);
            syncDelay(1000);
            location.reload();
	});
        $("#deleteTask").click(function(){
            var command = document.getElementById("command").value;
            var minute = document.getElementById("minute").value;
            var hour = document.getElementById("hour").value;
            var day = document.getElementById("day").value;
            var month = document.getElementById("month").value;
            var weekDay= document.getElementById("weekDay").value;

            $.post("/music/removeCronTask.sh", { command: command, minute: minute, hour: hour, day: day, month: month, weekDay: weekDay, userLogged: "'${userLogged}'"}, null);
            syncDelay(1000);
            location.reload();
        });
    });
</script>
</html>
'
