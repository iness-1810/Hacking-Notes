# Hack the box

1. Create your user in Hackthebox, and download the iso of kali, then decide wether you want the vmware hypervisor or virtualbox.
2. Once you create your username go to labs in the main page. Then you will need to choose between redteam (offensive) or blueteam(defensive) and go to first steps. My recommendation is to go to the first lesson called "meow".
3. Open your kali and access HTB with your account. Go to the simbol VPN, select “first lesson”, then OpenVpn and download your .ovpn .
4. Open the cmd of Linux , and execute sudo openVpn elnombredelarchivoquedescargaste and enter.
5. Now, if you go to the HTB page, the VPN symbol should appear in green. Time to start your first lesson.

# Meow
1. Go to meow and generate a “remote machine.” This will give you a secure IP to hack.
2. If you want, and for convenience, you can use mkdir to create a directory to save your tests. Once created, move inside using cd.
3. Ping <IPofcomputerattacking>. This is to find out if we have a secure connection to the computer we are attacking. A series of packets are sent (which you can stop with ctrl + c) and when it finishes running, most of them should have been received. Otherwise, the connection could be unstable.
4. With the command: nmap --min-rate=4000 -p -T5 -p allPorts.text, two important things will appear: which port is open and which OS is being used.
    *nmap: vulnerability search, --min... and -T3: to go faster, -p: to search all ports, -o: to create a new file -> example: nmap -p- thevulnerableportyouwanttoaccess --min-rate=4000 -T5 -o allPorts.text.
5. Now you must enter the new information you have received about the port name (telen, SMB, etc.) and the IP address. Use the commands -sc or -sv to obtain more information about the open port. In these first lessons, it is enough to know the username because the password is blank.
6. Explore everything and exit when you get the downloaded flag file. Return to your OS cmd with exit.
- if it is a redis port to acces to it: redis-cli -h 10.129.58.128 -p 6379
    - SELECT index : to move
    - KEYS *: print string
    - GET:  get resource
      
🌟 Tip: Open another CMD tab and type the command: "sudo su" to become superadmin 🌟


