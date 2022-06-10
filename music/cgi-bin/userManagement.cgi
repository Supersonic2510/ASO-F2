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
        <li><a href="/music/cgi-bin/monitoring.cgi">Monitoring</a></li>
        <li><a href="/music/cgi-bin/packetFiltering.cgi">Packet Filtering</a></li>
        <li><a href="/music/cgi-bin/schedulingManager.cgi">Scheduling Manager</a></li>
        <li><a href="/music/cgi-bin/logger.cgi">Logger</a></li>
    </ul>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
    <form>
        <label for="createUser">Create number:</label><br>
        <input type="text" id="createUser" name="createUser"><br>
        <label for="createPassword">Password:</label><br>
        <input type="password" id="createPassword" name="createPassword"><br>
        <input id="createUserButton" type="submit" value="Create User">
    </form>
    <form>
        <label for="deleteUser">Create number:</label><br>
        <input type="text" id="deleteUser" name="deleteUser"><br>
        <label for="deletePassword">Password:</label><br>
        <input type="password" id="deletePassword" name="deletePassword"><br>
        <input id="deleteUserButton" type="submit" value="Delete User">
    </form>
</body>

<script>
    //Jquerys
    $(document).ready(function(){
        $("#createUserButton").click(function(){
            var userValue = document.getElementById("createUser").value;
            var passwordValue = document.getElementById("createPassword").value;
            
            if (passwordValue.length == 0) {
                passwordValue = " ";
            }
            
            $.post("/music/createUser.sh", { user: userValue, password: passwordValue}, null);
        });
        $("#deleteUserButton").click(function(){
            var userValue = document.getElementById("deleteUser").value;
            var passwordValue = document.getElementById("deletePassword").value;
        
            if (passwordValue.length == 0) {
                passwordValue = " ";
            }
        
            $.post("/music/deleteUser.sh", { user: userValue, password: passwordValue}, null);
        });
    });
</script>
</html>
'
