import os

required_modules = ["pystyle", "colorama", "urllib.request", "sys", "bs4", "requests"]
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{module} not found. Installing now...")
        os.system(f"pip install {module}")
        __import__(module)

import requests, sys, datetime, urllib.request, platform, re
from colorama import Style, Fore, Back, init
from bs4 import BeautifulSoup

GB, YB, WB, IB = Back.GREEN, Back.YELLOW, Back.RED, Back.BLACK
g, c, y, r, b, w = Style.BRIGHT+Fore.GREEN, Style.BRIGHT+Fore.CYAN, Style.BRIGHT+Fore.YELLOW, Style.BRIGHT+Fore.RED, Style.BRIGHT+Fore.BLUE, Style.BRIGHT+Fore.LIGHTWHITE_EX

response = requests.get('https://free-proxy-list.net/')
pattern = re.compile(r'<tr><td>(\d+\.\d+\.\d+\.\d+)</td><td>(\d+)</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td><td>.*?</td></tr>')
matches = pattern.findall(response.text)

def cls():
    os.system('cls || clear')

def space():
    print("")

now = datetime.datetime.now()
dattt = now.strftime("%Y/%m/%d %H:%M:%S\n")
cls()
banner = f"""
{w}<{y}/{w}> {GB}{r}• Proxy Scrapper{Back.RESET}
{w}<{y}/{w}> {WB}{b}• Author : SIDDHU123M (GIT){Back.RESET}
{w}<{y}/{w}> {YB}{c}• Date and Time : {Back.RESET} {dattt}
"""

space()
print(banner)

httpsnum = ["https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all"]
sock4num = ["https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=1000&country=all"]
sock5num = ["https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=1000&country=all"]


def scrape():
    def scrape_proxies(url, file_obj):
        with urllib.request.urlopen(url) as response:
            file_obj.write(response.read())

    https = open('prox-https.txt', 'wb')
    socks4 = open('prox-socks4.txt', 'wb')
    socks5 = open('prox-socks5.txt', 'wb')

    for url, file_obj in zip(httpsnum + sock4num + sock5num, [https, socks4, socks5]):
        scrape_proxies(url, file_obj)

    https.close()
    socks4.close()
    socks5.close()
Arrow = Fore.WHITE
def count():
    files = {"Https.txt": "Http / Https", "Socks4.txt": "Socks4", "Socks5.txt": "Socks5"}
    for filename, name in files.items():
        with open(filename, 'r') as file:
            count = len(file.readlines())
            print(f"{Arrow}➤ {g}{name} Scrapped proxies: {count}")
    print()


    print(f"{Arrow}Thanks for using my tools <3\n")


def dupes():
    if platform.system() == 'Windows':
        os.system("type prox-https.txt | sort /unique > Https.txt")
        os.system("type prox-socks4.txt | sort /unique > Socks4.txt")
        os.system("type prox-socks5.txt | sort /unique > Socks5.txt")
    else:
        os.system("awk '!x[$0]++' prox-https.txt > Https.txt")
        os.system("awk '!x[$0]++' prox-socks4.txt > Socks4.txt")
        os.system("awk '!x[$0]++' prox-socks5.txt > Socks5.txt")

init()

import time

def progress_bar(percent):
    filled_blocks = int(percent / 10)
    empty_blocks = 10 - filled_blocks
    green_block = '\033[32m' + '▰' * filled_blocks + '\033[0m'
    white_block = '\033[97m' + '▱' * empty_blocks + '\033[0m'
    sys.stdout.write(f'\r{green_block}{white_block} {percent}% ')
    sys.stdout.flush()

scrape()
for percent in range(20, 110, 10):
    progress_bar(percent)
    time.sleep(0.5)

print("\n")
dupes()
urli = 'https://sslproxies.org/'
respons = requests.get(urli)
html_conten = respons.content
soup = BeautifulSoup(html_conten, 'html.parser')
table = soup.find('table', {'class': 'table table-striped table-bordered'})
rows = table.find_all('tr')

scraped = []

for row in rows[1:]:
    columns = row.find_all('td')
    ip = columns[0].text
    port = columns[1].text
    last_checked = columns[7].text
    if '1 min ago' in last_checked:
        #scraped.append(print(ip + ':' + port))
        with open('prox-https.txt', 'a') as f:
            f.write(ip + ':' + port)

with open('prox-https.txt', 'a') as f:
    for match in matches:
        ip_address = match[0]
        port = match[1]
        f.write(f'{ip_address}:{port}\n')

os.remove("prox-https.txt")
os.remove("prox-socks4.txt")
os.remove("prox-socks5.txt")
count()
