## Reversing

- Compilador de linux : `gcc -o` e indicas el ejecutable para compilarlo, `-g` pones todo para el debuggin, nombre de las funciones, variables, `-s` para no guardar ningún símbolos
- Pwntools: ret2win
- Leaks en memoria:
    - %x: 4 bytes -32 bits
    - %p: 8 bytes - 64 bits

| Arquitectura | Tamaño | Pwntools |
| --- | --- | --- |
| x86 (32-bit) | 4 bytes | `p32()` |
| x86-64 (64-bit) | 8 bytes | `p64()` |
| ARM32 | 4 bytes | `p32()` |
| ARM64 (Arch64) | 8 bytes | `p64()` |
- Símbolos - sirven para guiar al programador, el que hace el código
- Análisis dinámico con un debugger → gdb, con la extensión pwngdb
