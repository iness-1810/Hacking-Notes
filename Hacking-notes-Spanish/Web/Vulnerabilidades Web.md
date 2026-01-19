## Web

### SQL injection

[https://portswigger.net/web-security/sql-injection/cheat-sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

[https://hackviser.com/tactics/pentesting/web/sql-injection](https://hackviser.com/tactics/pentesting/web/sql-injection)

`sqlmap` → solo se puede exfiltrar información que esté implementado, en muchos casos funciona, pero en otros no funcionas, sobretodo en las complejas.

Poner comentarios
- `-- -`
- `/**/`
- `#`
  
Otros
- `*` para seleccionar todo
- UNION : junta dos columnas en la tabla con el mismo número de columnas

SELECT $\begin{cases} WHERE \\ IN \end{cases}$

### NoSQL injection

MongoDB

https://www.w3schools.com/mongodb/mongodb_query_operators.php

inyectar operadores adicionales : `Users.find({$and: [{username:"u"},{password:{$ne: "u"}}]})`

### Command injection

- ${IFS} espacios en blanco en bash
- `command1 || command2` Si comando1 falla, entonces se ejecuta comando2.
- this can also be done by a burpsuite request

### Blind Command injection

Objetivo: exfiltrar información aún si no vemos el resultado

- depending on the terminal being executed, execute files and impact the command terminal
  - `|| sleep x`  sirve para mirar si se está ejecutando algo pq espera `x` tiempo para ejecutar el comando y la página se queda esperando `x` tiempo
    - si le ponemos un condicionante depediento de esta espera `x` o `y` tiempo
    - a veces se usa `|| <command> ||`.
- para redirigir la salida: `> <ruta_dnd_puedes_escribir>/file.txt`  luego mirar el contenido con ayuda del repeater de burpsuite, ya q si por ejemplo es una imagen supuestamente no te va a poner nada en la web, pero en el repeater sí
- también vale utilizar el comando ping tipo:  `ping -c 10 127.0.0.1`
- a veces en el sitio del email en un feedback, cuestionario… se ejecutan comandos

### Cross Site Request Forgery

Un atacante podría enviar a una víctima un enlace o hacer que cargas una imagen en una página maliciosa que, al abrirla, hace una petición automática al servidor usando **tu sesión activa**.

Requisitos

1. existir una acción a realizar
2. La página utiliza Cookies
3. No existe un parámetro impredecible

Serverside Request Forgery

Herramienta de github con payloads: `gopherus`

### Subir archivos

`GIF89a;
<?php
echo “<pre>”;
readfile(“../../../../../../../../flag.txt”);
echo “</pre>”;
?>` to change the magic bytes and upload a malicious file


