import pyfiglet as pyfiglet

print(pyfiglet.figlet_format("NetScanner"))
baner = pyfiglet.figlet_format("by li0day")
print(baner)

print("Autor = li0day")
print("E-mail = li0day@tutanota.com")
print("Instagram = https://www.instagram.com/li0day/")
print("Wersja = 1.1")


import subprocess

def ping_ip(ip):
    (output, error) = subprocess.Popen((['ping', ip, '-n', '1']), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if b'bytes=32' in output:
        return "DZIALA"
    elif b'Destination host unreachable.' in output:
        return "BRAK ODPOWIEDZI"
    elif error:
        return "Blad DNS"
    else:
        return "NIEZNANY"
print("~" * 50)
addr = input("Podaj pierwsze 3 człony adresu IP np. XXX.XXX.XXX. : ")
a = input("Podaj poczatek zakresu skanowania od 1 do 999: ")
b = input("Podaj koniec zakresu skanowania od 1 do 999: ")
print("~" * 50)
for ip in range(int(a),int(b)+1):
    ip = str(addr)+str(ip)
    ip = ip.strip('\n')
    response = ping_ip(ip)
    result = ('%s,%s \n' % (ip, response))
    print(result)

