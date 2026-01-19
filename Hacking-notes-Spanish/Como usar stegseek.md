#Stego

##Stego Pasitos

🌟Si te descargas stegseek te va a otorgar una wordlist: rockyou.txt, esto es un documento con muchas contraseñas. Esto te sirve para descodificar un documento a fuerza bruta.
Pero, este documento puede presentarse como rockyou.txt.gz, gz es otro tipo de archivos Zip para Linux. (Tip: Para desbloquear archivos gz, necesitas ser sup admin (con sudo su) y ejecutar el comando gunzip junto con el nombre del archivo)

1. Una vez hecho esto puedes probar con stegseek --crack -sf nombredelarchivo.jpg -wl (esto es que va a inspeccionar un archivo wordlist) rockyou.tx. Importante estar en el mismo directorio que el archivo que vas a crackear
2. Te saldrá y desbloqueará una passphrase. Esto es una contraseña.
3. Con esa contraseña puedes desbloquear mediante el comando stegseek --crack -sf nombredelarchivo.jpg -p contraseña, los archivos ocultos.
4. Te saldrá un nuevo archivo en la carpeta que estaba. Prueba con ls para inspeccionarlo o cat si es un archivo para leerlo.
