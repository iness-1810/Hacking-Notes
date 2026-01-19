# Hack the box

1. Crea tu cuenta en Hackthebox, y descarga la iso de kali. Tienes que decidir que hipervisor vas a utilizar, mis recomendaciones son virtualbox o vmware.
2. Una vez creado el usuario de HTB , conectar con Labs en la opción de inicio. A partir de ahí selección el equipo rojo (ofensivos) y dale a primeros aprendizajes. Te debería salir una primera lección llamada “meow”.
3. A partir de ahora funcionaremos en la máquina virtual kali. Abre tu VM y entra en HTB con tu cuenta iniciada. Ves al simbolito que pone VPN, selecciona “first lesson”, luego OpenVpn y descarga el .ovpn.
4.Abre el cmd de Linux , siendo sudo, y ejecuta `openVpn elnombredelarchivoquedescargaste` y enter.
5. Ahora si vas a la pág HTB el símbolo de VPN debería salir en verde. Hora de empezar tu primera lección.

# Meow
1. Ves a meow y genera una “remote machine”. Esto te dará una IP segura a la que hackear.
2. Abre otra pestaña de CMD y escribe el comando: sudo su para pasar a ser superadmin
3. `ping <IP_del_ordenador_a_atacar>`. Esto sirve para saber si tenemos una conexión segura con el equipo que estamos atacando. Se envía una serie de paquetes (que puedes parar con ctrl + c) y cuando termine de ejecutarse deberían haberse recibido la mayoría. Sino la conexión podría ser inestable.
4. Con el comando: nmap --min-rate=4000 -p -T5 -p allPorts.text te saldrán dos cosas importantes, que puerto está abierto y que SO está utilizando. *nmap: búsqueda de vulnerabilidades, --min… y -T3: para ir más rápido , -p: para buscar en todos los puertos, -o : para crear un archivo nuevo -> ejemplo: nmap -p- elpuertovulnerablealquequierasacceder --min-rate=4000 -T5 -o allPorts.text.
5. Ahora debes ingresar con la nueva info que has recibido del nombre del puerto (telen, SMB…) y la IP, con los comandos -sc o -sv obtienes más info sobre el puerto abierto. En estas primeras lecciones basta con saber el usuario porque la contraseña es en blanco.
6. Explora todo y sal cuando consigas el archivo flag descargado. Vuelve con exit al cmd de tu SO.
- si es un puerto redis para acceder a él: redis-cli -h 10.129.58.128 -p 6379
   - SELECT index : para moverte
   - KEYS *: imprimir strings
   - GET:  conseguir un recursoe
      
🌟 Tip: Abre otra ventana CMD y escribe el comando `sudo su` para ser superadmin 🌟


