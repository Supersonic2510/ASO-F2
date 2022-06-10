#!/bin/bash
echo "Content-type: text/html"
echo '
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>User Managment</title>
  <ul>
    <li><a href="/music/cgi-bin/test.cgi">JuggerBox</a></li>
    <li><a href="/music/cgi-bin/register.cgi">Register</a></li>
    <li><a href="/music/cgi-bin/server.cgi">Server</a></li>
    <li><a href="/music/cgi-bin/monitoring.cgi">Monitoring</a></li>
    <li><a href="/music/cgi-bin/processManagement.cgi">Process Management</a></li>
    <li><a href="/music/cgi-bin/userManagement.cgi">User Management</a></li>
    <li><a href="/music/cgi-bin/packetFiltering.cgi">Packet Filtering</a></li>
    <li><a href="/music/cgi-bin/schedulingManager.cgi">Scheduling Manager</a></li>
  </ul>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
'
echo '<div>
  <h1>Logger Info</h1>
  <h4>Last 10 lines</h4>
  <article> ' 
  
    sudo tail -10 /var/log/syslog | while read line;do
      echo "${line} <br>"
      done

echo '
</article> 
</div>
</body>
</html>
'
