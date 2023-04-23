import requests, sys
import random, os
import csv
import concurrent.futures
import rich
from rich import print
from time import sleep

os.system('clear')
print("""[bold pale_turquoise1]\n
      ,------.                        ,--.          ,--.   
      |  .--. ',--.--. ,---.,--.  ,--.`--',--,--, ,-'  '-. 
      |  '--' ||  .--'| .-. |\  `'  / ,--.|      \'-.  .-' 
      |  | --' |  |   ' '-' '/  /.  \ |  ||  ||  |  |  |   
      `--'     `--'    `---''--'  '--'`--'`--''--'  `--'   
[/bold pale_turquoise1]
[magenta3]
  a tool to check if your url input excepts your proxys or not
[/magenta3]
[dark_orange]
                       (openpolicy0)
[/dark_orange]""")

print("[chartreuse1][NOTE!][/chartreuse1] [light_green]just add the name of the file not .csv[/light_green]")
file = input("PROXY FILE (.csv): ")
if os.path.exists('/home/kali/Proxint/'+file+'.csv'):
   print("[bold pale_turquoise1]proxy file found[/bold pale_turquoise1]")
else:
    print("[red1]file not found make sure it is a .csv file[/red1]")
    sys.exit()

protocol = input("http socks4 socks5: ")
if protocol=="http":
   print("[magenta3]adding http protocol[/magenta3]")
   sleep(1)
   print("[magenta3]Done press enter to start[/magenta3]")
   sleep(1)
   anykey=input("[ENTER]")

elif protocol=="socks4":
     print("[magenta3]adding socks4 protocol[/magenta3]")
     sleep(1)
     print("[magenta3]Done press enter to start[/magenta3]")
     sleep(1)
     anykey=input("[ENTER]")

elif protocol=="socks5":
     print("[magenta3]adding socks5 protocol[/magenta3]")
     sleep(1)
     print("[magenta3]Done press enter to start[/magenta3]")
     sleep(1)
     anykey=input("[ENTER]")

csv_f = file+".csv"

print("[light_green]===========================================================================[/light_green]")
sleep(1)
print("[light_green]scanning proxy IPs...[/light_green]")
sleep(1)
print("[light_green]IPs will be shown up or down[/light_green]")
sleep(1)
print("[light_green]using "+file+".csv containing proxys[/light_green]")
sleep(1)
print("""[light_green]

 IP status code | up or down | print proxy
==========================================
       200      |     ✅️     |   127.0.0.1
       404      |     ❌️     |    faild
[/light_green]""")
sleep(1)
print(" status code     |           WORKS       |         FROM IP ADDRESS")
print("=================================================================================")
file = []

with open(csv_f, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        file.append(row[0])

def extract(proxy):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={protocol : proxy,'https': proxy}, timeout=2)
        print('     200         |            UP ✅️      |             '+r.json()['origin'])
    except:
        print('     404         |           DOWN ❌     |             faild')
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, file)

print("[light_green]=(finding other proxys in your list)================================================[/light_green]")
sleep(1)
print("[light_green]=(simplifying proxys)===============================================================[/light_green]")
sleep(1)
print("[light_green]getting proxy IPs...[/light_green]")
sleep(1)
print("[light_green]getting region...[/light_green]")
sleep(2)
print("[light_green]getting country...[/light_green]")
sleep(2)
print("[light_green]===========================================================================[/light_green]")
with open(csv_f, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        file.append(row[0])

def extract(proxy):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        r = requests.get('https://ipinfo.io/json', headers=headers, proxies={protocol : proxy,'https': proxy}, timeout=2)
        print('     200         |       UP ✅️      |     '+r.json()['ip'], r.json()['region'], r.json()['country'])
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, file)

print("[light_green]===========================================================================[/light_green]")
sleep(1)
print("[light_green]Done[/light_green]")
