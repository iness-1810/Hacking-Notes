## Web

### SQL injection

[https://portswigger.net/web-security/sql-injection/cheat-sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

[https://hackviser.com/tactics/pentesting/web/sql-injection](https://hackviser.com/tactics/pentesting/web/sql-injection)

`sqlmap` → You can only exfiltrate information that is implemented. In many cases it works, but in others it doesn't, especially in complex cases.

Put comments
- `-- -`
- `/**/`
- `#`
  
Other
- `*` to select all
- UNION : join two columns in the table with the same number of columns

SELECT $\begin{cases} WHERE \\ IN \end{cases}$

### NoSQL injection

MongoDB

https://www.w3schools.com/mongodb/mongodb_query_operators.php

inyect additional operators : `Users.find({$and: [{username:"u"},{password:{$ne: "u"}}]})`

### Command injection

- ${IFS} blank spaces in bash
- `command1 || command2` if command1 fails, then command2 is executed.
- this can also be done by a burpsuite request

Exfiltrate information even if we don't see the result

- depending on the terminal being executed, execute files and impact the command terminal

### Blind Command injection

- `|| sleep x` is used to check if something is running because it waits `x` time to execute the command and the page waits `x` time
- if we add a condition depending on this, it waits `x` or `y` time
    - Sometimes `|| <command> ||` is used.
- To redirect the output: `> <path_you_can_write>/file.txt`  Then view the content using the Burp Suite repeater, since if it is an image, for example, it will not show anything on the web, but it will show up in the repeater.
- You can also use the ping command, such as: `ping -c 10 127.0.0.1`
- Sometimes commands are executed on the email site in feedback, questionnaires, etc.

### Cross Site Request Forgery

An attacker could send a victim a link or make them load an image on a malicious page that, when opened, makes an *automatic* request to the server using **your active session**.

Requirements

1. There must be an action to perform.
2. The page uses cookies.
3. There is no unpredictable parameter.

Serverside Request Forgery

GitHub tool with payloads: `gopherus`

### File Upload

`GIF89a;
<?php
echo “<pre>”;
readfile(“../../../../../../../../flag.txt”);
echo “</pre>”;
?>` to change the magic bytes and upload a malicious file

