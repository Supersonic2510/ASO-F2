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
        <li><a href="/music/cgi-bin/server.cgi">Server</a></li>
        <li><a href="/music/cgi-bin/processManagement.cgi">Process Managment</a></li>
        <li><a href="/music/cgi-bin/userManagement.cgi">User Management</a></li>
        <li><a href="/music/cgi-bin/monitoring.cgi">Monitoring</a></li>
	<li><a href="/music/cgi-bin/packetFiltering.cgi">Packet Filtering</a></li>
	<li><a href="/music/cgi-bin/schedulingManager.cgi">Scheduling Manager</a></li>
	<li><a href="/music/cgi-bin/logger.cgi">Logger</a></li>
    </ul>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
  <form>
      <label for="fname">UserName:</label><br>
      <input type="text" id="userName" name="userName"><br>
      <label for="lname">Password:</label><br>
      <input type="password" id="password" name="password"><br><br>
      <button id="logInButon" >Log In</button>
  </form>
</body>
</html>

<script>   
    //Jquerys
    $(document).ready(function(){
        $("#logInButon").click(function(){
          var userName = document.getElementById("userName").value;
	  var passwordPost = document.getElementById("password").value;
            $.post("/music/logInUser.sh", {username: userName, password: passwordPost}, null);
        });
    });
</script>
'
