#!/bin/bash
echo "Content-type: text/html"
echo '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register Page</title>
    <ul>
        <li><a href="/music/cgi-bin/test.cgi">JuggerBox</a></li>
        <li><a href="/music/cgi-bin/register.cgi">Register</a></li>
        <li><a href="/music/cgi-bin/processManagement.cgi">Process Management</a></li>
        <li><a href="/music/cgi-bin/userManagement.cgi">User Management</a></li>
        <li><a href="/music/cgi-bin/monitoring.cgi">Monitoring</a></li>
        <li><a href="/music/cgi-bin/packetFiltering.cgi">Packet Filtering</a></li>
        <li><a href="/music/cgi-bin/schedulingManager.cgi">Scheduling Manager</a></li>
        <li><a href="/music/cgi-bin/logger.cgi">Logger</a></li>
    </ul>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
  <button id="shutDownButton" >Shut Down</button>
  <button id="restartButton" >Restart</button>
</body>
</html>

<script>
    //Jquerys
    $(document).ready(function(){
        $("#restartButton").click(function(){
            $.post("/music/restartServer.sh", null, null);
        });
        $("#shutDownButton").click(function(){
            $.post("/music/shutDownServer.sh", null, null);
        });
    });
</script>
'

