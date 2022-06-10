#!/bin/bash
echo "Content-type: text/html"

if [ "$REQUEST_METHOD" = "POST" ]; then
    if [ "$CONTENT_LENGTH" -gt 0 ]; then
        read queryString
        saveIFS=$IFS
        IFS='=&'
        arrayKeys=($queryString)
        IFS=$saveIFS	

		if [[ ${arrayKeys[0]} = pidKill ]];then
			pidKill=${arrayKeys[1]}
		elif [[ ${arrayKeys[0]} = pid ]] && [[ ${arrayKeys[2]} = seconds ]];then
		  status=$(ps -p $pid -o pid,vsz=MEMORY -o user,group=GROUP,state=STATE,time=TIME -o comm,args=ARGS)
		fi
    fi
fi

echo '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title><!DOCTYPE html>
      <html lang="en">
      <head>
      <meta charset="UTF-8">
      <title>Register Page</title>
  <ul>
    <li><a href="/music/cgi-bin/test.cgi">JuggerBox</a></li>
    <li><a href="/music/cgi-bin/register.cgi">Register</a></li>
    <li><a href="/music/cgi-bin/server.cgi">Server</a></li>
    <li><a href="/music/cgi-bin/userManagement.cgi">User Management</a></li>
    <li><a href="/music/cgi-bin/monitoring.cgi">Monitoring</a></li>
    <li><a href="/music/cgi-bin/packetFiltering.cgi">Packet Filtering</a></li>
    <li><a href="/music/cgi-bin/schedulingManager.cgi">Scheduling Manager</a></li>
    <li><a href="/music/cgi-bin/logger.cgi">Logger</a></li>
  </ul>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>

<div style="height:600px;width:540px;border:1px solid #ccc;font:16px/26px Georgia, Garamond, Serif;overflow:auto;">
'
echo $(ps aux | awk {'printf "<p>	  · %s %s </p>",$11, $2'})
echo '
</div>

<form>
  <label for="pid">PID number:</label><br>
  <input type="number" id="pid" name="pid"><br>
  <label for="seconds">Interruption seconds:</label><br>
  <input type="number" id="seconds" name="seconds"><br>
  <input id="queryStatusButton" type="submit" value="Query Status">
</form>
<form method="post" action="?">
  <label for="pidKill">PID number:</label><br>
  <input type="number" id="pidKill" name="pidKill"><br>
  <input id="killPIDButton" type="submit" value="Kill PID">
</form>

'
echo -e "<p> Process status</p>"
echo -e "<article>$status</article>"
echo '

</body>
</html>
<script>
    //Jquerys
    $(document).ready(function(){
        $("#queryStatusButton").click(function(){
	    let value = document.getElementById("pid").value;
        $.post("/music/interruptPID.sh", {number: value}, null);
        });
    });
</script>
'
