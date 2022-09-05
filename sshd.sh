#!/usr/bin/env bash

echo "Welcome to securing the ssh script"
echo "!---Make sure this user have write permissions for the ssh_config file---!"
echo "Please enter the port number"
read PORT
if [ ${PORT} -gt -1 ] && [ ${PORT} -lt 65536 ]
then 
	#Adding a new Port comand that will over-rule the old one as it comes after it
	#---- This doesn't change the value of the old variable ----
	
	echo "Port ${PORT}" >> /etc/ssh/ssh_config
	echo "ssh port number in sshd_config is updated to ${PORT}"
	echo "PermitRootLogin no" >>  /etc/ssh/ssh_config
	echo "Permitted root login in ssh"
 else
 	echo "The enterd port is outside the accepted range"
fi
