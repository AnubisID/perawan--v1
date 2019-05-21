#recode gak akan buat lu menjadi pro bangsat !!!
#rekode auto mandul!!!!!


from urllib.request import urlopen, Request, URLError, HTTPError
import sys
import time
print('''\033[93m
            _       _           _         _             _       
           / \   __| |_ __ ___ (_)_ __   | | ___   __ _(_)_ __  
          / _ \ / _` | '_ ` _ \| | '_ \  | |/ _ \ / _` | | '_ \ 
         / ___ \ (_| | | | | | | | | | | | | (_) | (_| | | | | |
        /_/   \_\__,_|_| |_| |_|_|_| |_| |_|\___/ \__, |_|_| |_|
                                                  |___/         
''')
def hp(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(5./100)
hp(            "___________________________________________")
hp(            "| judul   : Mencari rumah perawan         |")
hp(            "| Author  : Mr.p3rc1l                     |")
hp(            "| Team    : CRAZY HACK TEAM               |")
hp(            "| thanks  : Mr.r1dw4n & Mr.panjul21       |")
hp(            "|_________________________________________|")
header = {'user-agent': 'Moofzilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
file = open('Admin.txt', 'r').read().split('\n')
site = input('\033[95mMasukan alamat yang perawan: ')
hp("\033[94mMencari jalan rumah perawa...\033[0m")
for list in file:
    url = site  +list
    try:
        req = Request(url, None, header)
        res = urlopen(req)
    except(ValueError, HTTPError, URLError):
        print('\033[31;1msalah alamat bego: ' + url + '\033[0m')
    else:
        print('\033[32;1mnah ketemu rumah nya: ' + url + '\033[0m')
