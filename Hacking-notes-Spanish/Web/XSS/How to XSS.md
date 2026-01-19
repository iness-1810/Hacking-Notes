### Inyecciones html - XSS

[https://xss-game.appspot.com/level2](https://xss-game.appspot.com/level2)

`<!-- Esto es un comentario -->`

xss payloads all the things

En la consola

1. `<i>hola</i>` cursivas, contenido simple
2. `<script>alert(1)</script>` solo se ejecuta cuando el navegador ejecuta la página completa
3. `<img src=>` insertar contenido
4. `<img src=xyz onerror='alert("hola")'>` insertar código, con un cargador de eventos, si el contenido falla en cargar la imagen salta la alerta
    
    `document.cookie` recuperar cookies, exfiltrarlas
    
5. `frame#123' onerror='alert("hola")'` inyectarlo en la url
6. `frame#123'> <onerror='alert("hola")'`> inyectarlo en la url

`<script>alert(1)</script>`  es como echo

Reflected XSS

- Si no sanitizas la entrada y una app recibe datos de una petición HTTP y lo devuelve directamente en la respuesta. Es decir, si el contenido se ve en el cuerpo de la petición, está en la url

Stored XSS

- Se queda en la base de datos
- meter el prompt dentro de lo que hace la consulta a la base de datos

Dom-Based XSS

- mirar donde se está cargando el input, está todo en la página tan cual
- JavaScript es el encargado de procesar la petición escribiéndolo sin validación → mirar javascript
- `"><script>alert(1)</script>`

Angular js

- Si pone ng-app es que está utilizando angular
- Angular es un framework de javascript

Escapar de cadenas de texto en Js

- mirar cadena y poner `//` para comentar el resto