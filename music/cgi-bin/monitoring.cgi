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
    <li><a href="/music/cgi-bin/processManagement.cgi">Process Management</a></li>
    <li><a href="/music/cgi-bin/userManagement.cgi">User Management</a></li>
    <li><a href="/music/cgi-bin/packetFiltering.cgi">Packet Filtering</a></li>
    <li><a href="/music/cgi-bin/schedulingManager.cgi">Scheduling Manager</a></li>
    <li><a href="/music/cgi-bin/logger.cgi">Logger</a></li>
  </ul>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
'
echo '<div>
  <h1>CPU Info</h1>
  <article> ' 
  i=0
    mpstat | while read line;do
      echo "${line} <br>"
      if [[ $i -eq 0 ]] ||  [[ $i -eq 2 ]];then
        echo "<br>"
      fi
      i=$(($i+1))
      done
echo  '</article>
</div>
<div>
  <h1>Memory Info</h1>
  <article> '  
  i=0
    cat /proc/meminfo | while read line;do
      echo "${line} <br>"
      if [[ $i -eq 0 ]];then
        echo "<br>"
      fi
      i=$(($i+1))
      done
echo ' </article>
</div>
<div>
  <h1>Disk Info</h1>
  <article>'
    i=0
    df -h | while read line;do
      echo "${line} <br>"
      if [[ $i -eq 0 ]];then
        echo "<br>"
      fi
      i=$(($i+1))
      done
echo    '
  </article>
</div>

<div>
  <h1>Last access</h1>
  <article>'
    echo "User Command Line IP Date<br><br>"
    last | tail -10 | while read line;do
      echo "${line} <br>"
      done

echo '
</div>
</body>
</html>
'
