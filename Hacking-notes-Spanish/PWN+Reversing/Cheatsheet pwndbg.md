# Cheatsheet pwndbg

| Comando | Qué hace | Argumentos / sintaxis | Ejemplo / nota |
| --- | --- | --- | --- |
| `info functions` | Lista las funciones que GDB conoce (del binario y, si aplica, de librerías con símbolos). | No requiere argumentos. Opcionalmente puedes filtrar por patrón (según versión/config). |  |
| `disassemble` | Muestra el desensamblado (instrucciones ensamblador) de una función. | `\<nombre_función\>` | `disassemble main` |
| `break` `b` | Crea un breakpoint al inicio de la función indicada o pone un breakpoint en una dirección exacta (breakpoint “por dirección”). | `*<dirección_de_memoria>`dirección  (`0x...`) o una expresión,    `*<función+offset>` o`<archivo>:<línea>` o `<nombre_función>` | `break vuln` ,  `b *0x40123a` o `b *main+42`,si lo que querías era “línea de código”, suele ser `break archivo.c:123` (sin `*`). |
| `run` | Arranca el programa desde el principio (y se parará en el primer breakpoint que encuentre). | `run [args_del_programa]` | `run` o `run input.txt` |
| `c` (continue) | Continúa la ejecución hasta el siguiente breakpoint, señal, o fin del programa. | Sin argumentos: `c` | Nota: no “salta a la próxima función” necesariamente; sigue hasta el próximo punto de parada. |
| `n` (next) | ejecuta la **siguiente línea** y, si hay una llamada a función, **no entra** dentro (la ejecuta y se para en la línea siguiente). | `<nº_pasos>` | si estás en una línea con `printf(...)`, `n` ejecuta el `printf` y se detiene en la siguiente línea. Para entrar en la función: `s` (step) |
| `set *(int *)($rbp-4) = 0270f` | Modifica memoria: escribe un entero (`int`) en la dirección calculada a partir de `$rbp-4`. | `set <expresión>= <valor>` (aquí la expresión es un *cast* y un *dereference*). | Nota: `0270f` se interpreta como número en base según el prefijo/formato; si quieres hexadecimal de forma clara, suele usarse `0x270f`. |
| `x /xv $rbp-4` | Examina memoria en la dirección `$rbp-4` mostrando el contenido. | `/formato` `<lugar_de_la_memoria\>`.
Aquí: `/x` = hexadecimal, `v` = “verbose” (según extensión/versión). | `x /xv $rbp-4`
Variantes típicas: `x/wx $rbp-4` (1 word en hex), `x/gx ...` (8 bytes en hex). |
| `python print()` también puedes hacer `python payload=b"A"*72` | Escribe 72 o las veces que quieras un carácter | `"A" * <nº_veces_que_quieras\\\>` | `python print("A"*72)` |
| `cyclic` | Escribe un patrón cíclico fácil de observar en el heap | `-l <dirección_de_memoria>` o `<nº_letras>` | `cyclic 100 payload` escribe un texto cíclico en el archivo payload |
| `ltrace` | Muestra las llamadas a librerías (por ejemplo `printf`, `strcmp`, `malloc`) que hace el programa y sus argumentos/valores devueltos. | `ltrace [opciones] <programa> [args]` Útiles: `-p <pid>` (adjuntarse), `-f` (seguir forks), `-e <filtro>` (filtrar funciones). | `ltrace ./binario`</br> `ltrace -e strcmp+strlen ./binario` |
