from os import system as cmd
from sys import exit
from colorama import Fore
from time import sleep as wait
import requests
from bs4 import BeautifulSoup as bs

def debugcolor():
    print(Fore.WHITE + '.')
    cmd('cls')

def cmdclear():
    print(' Cleaning the console...')
    wait(0.2)
    cmd('cls')
    print(' Basics commnads: \n')
    print(guide)

def remove(spaces):
    return spaces.replace(".", "")

nolink = 'https://es.wallapop.com/electronica/portatil'
url = requests.get(nolink).text
soup = bs(url, 'html.parser')

# Info page
'''
Price class -> product-info-price
Tittle class -> product-info-title
Bio class -> product-info-description1
'''

lsprices = [] # 40
lstittles = [] #lstittles[n][25:-21] For no spaces | 40
lsbios = [] # 40
lslinks = [] # lsprices[0] == lslinks[8] | 92

prices = soup.find_all('span', class_ = 'product-info-price')
tittles = soup.find_all('span', class_='product-info-title')
bios = soup.find_all('p', class_='product-info-description')
links = soup.find_all('a')

for price in prices:
    i = price.string
    lsprices.append(i)

lspriceint = []

for i in lsprices:
    global lvprlmpdm
    lvprlmpdm = remove(i)
    lspriceint.append(lvprlmpdm)

for i in lspriceint:
    lsprices.append(i)

del lsprices
for tittle in tittles:
    i = tittle.string
    lstittles.append(i)

for bio in bios:
    i = bio.string
    lsbios.append(i)

for enlace in links:
    x = enlace.get('href')
    lslinks.append(x)

#Start the bot script
cmd('cls')
logo = '''  _    _       _ _                           _           _   
 | |  | |     | | |                         | |         | |  
 | |  | | __ _| | | __ _ _ __   ___  _ __   | |__   ___ | |_ 
 | |/\| |/ _` | | |/ _` | '_ \ / _ \| '_ \  | '_ \ / _ \| __|
 \  /\  / (_| | | | (_| | |_) | (_) | |_) | | |_) | (_) | |_ 
  \/  \/ \__,_|_|_|\__,_| .__/ \___/| .__/  |_.__/ \___/ \__|
                        | |         | |                      
                        |_|         |_|                      '''

global guide

guide = ''' [1]- Start
 [2]- Select price
 [3]- Command lists
 [4]- Print this guide
 [5]- Exit
'''

blackguide = '''\n Commnads lists
 -> select *number*: Give back the wallapop link
 -> category *category*: Change the list to another category
 -> clear: Clean the console
 -> fquit: Force quit
 -> rcls: Reset colors of console [If it bugs]
'''

print(logo)
print(guide)

while True:
    x = input(' Walafross $> ').split(" ")

    # Loop for the big list / Variables of those
    wholelist =[]
    tittl3 = 0
    pric3 = 0
    bi0 = 0
    l1nk = 8
    
    for i in range(len(lstittles)): #Len of all lists
        wholelist.append([lstittles[tittl3][25:-21], lspriceint[pric3], lsbios[bi0]])
        tittl3 += 1; pric3 += 1; bi0 += 1; l1nk += 1

    if x[0] == '1':   
        try: 
            inum = 0
            while inum < len(lstittles):
                print(f'\n {inum+1} -',*wholelist[inum], sep= ' | ')
                inum += 1
        except:
            pass

    elif x[0] == '2':
        guid1 = ''' 
         -> mxp *number*: Limit the maximun price
         -> mnp *number*: Liminit the minimun price
         -> 3max: Print the 3 most expensive
         -> 3min: Print the 3 less expensive
        '''

        print(guid1)

    elif x[0] == '4':
        print(guide)

    elif x[0] == '5':
        cmd('cls')
        print(Fore.LIGHTBLACK_EX + '''  _  _  ____  ____    _  _   __   __     __   ____  ____   __   ____  ____     __    ___   __   __  __ _  _  _  _   
 / )( \/ ___)(  __)  / )( \ / _\ (  )   / _\ (  __)(  _ \ /  \ / ___)/ ___)   / _\  / __) / _\ (  )(  ( \/ \/ \/ \  
 ) \/ (\___ \ ) _)   \ /\ //    \/ (_/\/    \ ) _)  )   /(  O )\___ \ \__ \  /    \( (_ \/    \ )( /    /\_/\_/\_/  
 \____/(____/(____)  (_/\_)\_/\_/\____/\_/\_/(__)  (__\_) \__/ (____/(____/  \_/\_/ \___/\_/\_/(__)\_)__)(_)(_)(_) ''')
        wait(1)
        exit()
    

    # List commands

    elif x[0] == '3':
        print(blackguide)

    elif x[0] == 'help':
        print(blackguide)

    elif x[0] == 'select':
        
        if int(x[1]) < 0:
            print('You can`t use a negative number...\n')

        elif int(x[1])-1 < len(wholelist):
            print(f' \n {Fore.LIGHTBLACK_EX}Tittle: {Fore.WHITE + wholelist[int(x[1])-1][0]}      {Fore.LIGHTBLACK_EX}Price: {Fore.WHITE + wholelist[int(x[1])-1][1]}')
            print(f' {Fore.LIGHTBLACK_EX}Bio: {Fore.WHITE + wholelist[int(x[1])-1][2]}\n')
            print(f' {Fore.LIGHTBLACK_EX}Link: {Fore.WHITE}https://es.wallapop.com{Fore.WHITE + lslinks[int(x[1])-1+8]}\n')

        else:
            print('The object doesn`t exists, try with a lower number')

    elif x[0] == 'mxp':
        if int(x[1]) < len(wholelist):
            y = int(x[1])
            z = 0
            for i in range(len(wholelist)):
                if y >= float(wholelist[z][1][0:-4]):
                    print(f'\n{z+1} -',*wholelist[z],sep= ' | ')
                z += 1

        else:
            pass

    elif x[0] == 'mnp':
        if int(x[1]) < len(wholelist):
            y = int(x[1])
            z = 0
            for i in range(len(wholelist)):
                if y <= int(wholelist[z][1][0:-4]):
                    print(f'\n{z+1} -',*wholelist[z],sep= ' | ')
                z += 1

    elif x[0] == 'category':
        print(f'{Fore.RED} This part is in mantenimient, please try later... {Fore.WHITE}')
        pass

    elif x[0] == 'clear':
        cmdclear()
    
    elif x[0] == 'cls':
        cmdclear()

    elif x[0] == 'fquit':
        exit()

    elif x[0] == 'rcls':
        debugcolor()

    else:
        print(' Check the commmands with: 4')