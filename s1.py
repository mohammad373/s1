# s1
# https://api.hackertarget.com/whois/?q=
import os
import sys
import time
import requests
from colorama import Fore

def __target__():
    os.system("clear")
    time.sleep(1)
    print(Fore.YELLOW + "Hi , I`m Bobot ;))")
    time.sleep(1)
    target = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Pleass Enter Domain" + Fore.GREEN + " ==>  ")
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Domain Is None ;(")
            time.sleep(1)
            sys.exit()
        except:
            sys.exit()
    r1 = requests.get("https://api.hackertarget.com/whois/?q=" + target)
    if r1.status_code != 200:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Domain Is Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            sys.exit()
    else:
        print(r1)
        time.sleep(1)
        sys.exit()
__target__()
