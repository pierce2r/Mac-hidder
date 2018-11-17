import sys,os
import random

colour=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m']
normal=('\033[1;m')

try:
    # creating banner
    def banner():
        print('*'*80)
        print(random.choice(colour)+'Created by Pierce2r'+normal).center(100)
        print(random.choice(colour)+'Lets hide it'+normal).center(100)
        print('*'*80)
    # hiding file
    def hide():
        os.system('chflags hidden '+h)
        print(random.choice(colour)+'[+] successfully Hidden'+normal)
    # unhidding file
    def unhide():
        os.system('chflags nohidden '+unh)
        print(random.choice(colour)+'[+] successfully unhidden'+normal)

    banner()
    print('Do you want to hide or unhide folder on your Mac: ')
    print('[1] Hide folder')
    print('[2] Unhide folder')
    print('')
    ask=raw_input('choose: ')
    if ask == '1':
        hd = raw_input("Drag folder or file to hide here:")
        h = hd[0:-1]
        os.system('mkdir ~/Documents/hide/')
        file = open('./Documents/hide/hide.txt','a')
        file.write(h)
        file.close()
        print(random.choice(colour)+'[*] link saved to ~/Documents/hide/hide.txt'+normal)
        hide()

    if ask == '2':
        unhd = raw_input("Drag folder or file to unhide here:")
        unh = unhd[0:]
        unhide()

except KeyboardInterrupt():
    print('exitting...')
    os.system('clear')
