import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
os.system('xdg-open https://web.facebook.com/anonymousproo1')
logo =("""\033[92m●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●█████████●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●█████████\033[92m 

\033[94m		 ███████████ ███████████ \033[94m
\033[94m		░░███░░░░░░█░░███░░░░░███\033[94m
\033[94m		 ░███   █ ░  ░███    ░███\033[94m
\033[94m		 ░███████    ░██████████ \033[94m
\033[94m		 ░███░░░█    ░███░░░░░███\033[94m
\033[94m		 ░███  ░     ░███    ░███\033[94m
\033[94m		 █████       ███████████ \033[94m
\033[94m		░░░░░       ░░░░░░░░░░░  \033[94m
                         
\x1b[38;5;46m   █████████                               █████ \x1b[1;97m                       
\x1b[38;5;46m  ███░░░░░███                             ░░███                         
\x1b[38;5;46m ███     ░░░  ████████   ██████    ██████  ░███ █████  ██████  ████████ \x1b[1;97m
\x1b[38;5;46m░███         ░░███░░███ ░░░░░███  ███░░███ ░███░░███  ███░░███░░███░░███\x1b[1;97m
\x1b[38;5;46m░███          ░███ ░░░   ███████ ░███ ░░░  ░██████░  ░███████  ░███ ░░░ \x1b[1;97m
\x1b[38;5;46m░░███     ███ ░███      ███░░███ ░███  ███ ░███░░███ ░███░░░   ░███     \x1b[1;97m
\x1b[38;5;46m ░░█████████  █████    ░░████████░░██████  ████ █████░░██████  █████    \x1b[1;97m
\x1b[38;5;46m  ░░░░░░░░░  ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░    \x1b[1;97m 

\033[92m●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●█████████●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●█████████\033[92m 
                                            
\033[41m \033[1;37m           [MAHFUZUR RAHMAN]               \x1b[0m
\033[1;32m┌●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●█████████●▬▬▬▬▬▬▬▬▬๑┐   
\033[1;33m│ [🔥] Admin   : MAHFUZUR RAHMAN\033[1;32m       │
\033[1;36m│ [🔥] TEAM    :BD D4RK TEAM H4CKER │ 	
\033[1;34m│ [🔥] Github  :\033[41m\033[1;37manonymousproo\x1b[0m     │
\033[1;35m│ [🔥] Whtsapp : +15715652343             │
\033[1;36m│ [🔥] Youtube : \x1b[38;5;46mCOMING SOON\x1b[1;97m        │ 
\033[1;36m│ [🔥] Facebook: \x1b[38;5;46manonymousproo1\x1b[1;97m      │ 	
\033[1;36m│ [🔥] Version : \x1b[38;5;46 .3.1v\x1b[1;97m      │ 						           │               
\033[1;32m└●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●█████████●▬▬▬▬▬▬▬▬▬๑┘   
\033[1;94m●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●
\033[1;97m     Status : \033[38;5;46mPAID 3.1V
\033[1;94m●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●  """)

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[92m[01]📱Random Number Clone\033[92m")
        print("\033[92m[02]📧Random Email Clone\033[92m")
        print("\x1b[38;5;196m[00]🛑Exit\033[31m")
        print("\033[1;32m ●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●●▬▬▬▬▬▬▬▬▬๑🔥๑▬▬▬▬▬▬▬▬●")
        Mumit =input("\033[92m [?] Choose : \033[92m")
        os.system('xdg-open https://github.com/anonymousproo')
        if Mumit in ["1", "01"]:
            num()
        if Mumit in ["2","02"]:
            gml()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    
        
        #sys.stdout.write(f'\r\033[m[DARK] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        #sys.stdout.flush()
    
        
Main()
