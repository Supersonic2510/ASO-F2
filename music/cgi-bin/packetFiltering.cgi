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
        <li><a href="/music/cgi-bin/schedulingManager.cgi">Scheduling Manager</a></li>
        <li><a href="/music/cgi-bin/logger.cgi">Logger</a></li>
    </ul>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
<article>
<h2>IP Table:</h2>
'
      i=-1
      j=1
      sudo iptables -L INPUT -v -n | more | while read line;do
      if [[ $i -gt 0 ]];then
        echo "Line ${j}: ${line} <br>"
        j=$(($j+1))
      else
        echo "${line} <br>"
      fi
      if [[ $i -eq 0 ]];then
        echo "<br>"
      fi
      i=$(($i+1))
      done
      
      echo "<br>"
      
      i=-1
      j=1
      sudo iptables -L OUTPUT -v -n | more | while read line;do
      if [[ $i -gt 0 ]];then
        echo "·Line ${j}: ${line} <br>"
        j=$(($j+1))
      else
        echo "   ${line} <br>"
      fi
      if [[ $i -eq 0 ]];then
        echo "<br>"
      fi
      i=$(($i+1))
      done
      
      echo "<br>"
      
      i=-1
      j=1
      sudo iptables -L FORWARD -v -n | more | while read line;do
      if [[ $i -gt 0 ]];then
        echo "Line ${j}: ${line} <br>"
        j=$(($j+1))
      else
        echo "   ${line} <br>"
      fi
      if [[ $i -eq 0 ]];then
        echo "<br>"
      fi
      i=$(($i+1))
      done

echo "
</article>
    <form>
        <h2>IP Rule:</h2>
        <label for="IPSource">IP Source:</label><br>
        <input type="text" id="IPSource" name="addIPSource"><br>
        <label for="IPDest">IP Dest:</label><br>
        <input type="text" id="IPDest" name="addIPDest"><br>
        IP Protocol:<br>
        <select name="IPProtocol" id="IPProtocol">
            <option value="" selected>None</option>
            <option value="tcp">TCP</option>
            <option value="udp">UDP</option>
        </select><br>
        <label for="IPPort">IP Port:</label><br>
        <input type="number" id="IPPort" name="addIPPort"><br>
        <label for="IPPosition">IP Rule Position:</label><br>
        <input type="number" id="IPPosition" name="IPPosition" min="1"><br>
        IP Type:<br>
        <select name="IPProtocol" id="IPType">
            <option value="ACCEPT" selected>Accept</option>
            <option value="REJECT">Reject</option>
            <option value="DROP">Drop</option>
            <option value="QUEUE">Queue</option>
            <option value="RETURN">Return</option>
        </select><br>
        Modify/Remove Type:<br>
        <select name="IPProtocol" id="IPTypeRemMod">
            <option value="INPUT" selected>Input</option>
            <option value="OUTPUT">Output</option>
            <option value="FORWARD">Forward</option>
        </select><br>
        <input id="addIPRule" type="submit" value="Add Rule">
        <input id="modifyIPRule" type="submit" value="Modify Rule"><br>
        <input id="deleteIPRule" type="submit" value="Remove Rule">
    </form>
"

echo '
</body>
<script>
    //Jquerys
    $(document).ready(function(){
        $("#addIPRule").click(function(){
            var ipSource = document.getElementById("IPSource").value;
            var ipDest = document.getElementById("IPDest").value;
            var ipProtocol = document.getElementById("IPProtocol").value;
            var ipPort = document.getElementById("IPPort").value;
            var ipPosition = document.getElementById("IPPosition").value;
            var ipType = document.getElementById("IPType").value;
            var typeRemMod = document.getElementById("IPTypeRemMod").value;
            $.post("/music/addIPTable.sh", { IPPosition: ipPosition, IPSource: ipSource, IPDest: ipDest, IPProtocol: ipProtocol, IPPort: ipPort, type: ipType, remModTpe: typeRemMod}, null);
        });
        $("#modifyIPRule").click(function(){
            var ipSource = document.getElementById("IPSource").value;
            var ipDest = document.getElementById("IPDest").value;
            var ipProtocol = document.getElementById("IPProtocol").value;
            var ipPort = document.getElementById("IPPort").value;
            var ipPosition = document.getElementById("IPPosition").value;
            var ipType = document.getElementById("IPType").value;
            var typeRemMod = document.getElementById("IPTypeRemMod").value;
            $.post("/music/modifyIPTable.sh", { IPPosition: ipPosition, IPSource: ipSource, IPDest: ipDest, IPProtocol: ipProtocol, IPPort: ipPort, type: ipType, remModTpe: typeRemMod}, null);
        });
        $("#deleteIPRule").click(function(){
            var ipSource = document.getElementById("IPSource").value;
            var ipDest = document.getElementById("IPDest").value;
            var ipProtocol = document.getElementById("IPProtocol").value;
            var ipPort = document.getElementById("IPPort").value;
            var ipPosition = document.getElementById("IPPosition").value;
            var ipType = document.getElementById("IPType").value;
            var typeRemMod = document.getElementById("IPTypeRemMod").value;
            $.post("/music/removeIPTable.sh", { IPPosition: ipPosition, IPSource: ipSource, IPDest: ipDest, IPProtocol: ipProtocol, IPPort: ipPort, type: ipType, remModTpe: typeRemMod}, null);
        });
    });
</script>
</html>
'
