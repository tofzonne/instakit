import instaloader
from getpass import getpass
from core.init import Print, getimg, info, downloadPost, clear_sc

def banner():
    print("""
\033[1;32m
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗  ██╗██╗████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║ ██╔╝██║╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║█████╔╝ ██║   ██║   
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔═██╗ ██║   ██║   
██║██║ ╚████║███████║   ██║   ██║  ██║██║  ██╗██║   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   
            \033[0m""")



login = False
L = instaloader.Instaloader()

clear_sc()
banner()
Print('w', '1. Login')
Print('w', '2. Without Login...\n\n\n')
opt = input()

if opt.strip()[0] == '1':
    clear_sc()
    banner()
    Print('i', 'To login Enter the credentials Below\n')
    user = input('Username: ')
    pwd = getpass()

    try:
        print()
        Print('i', 'Please Wait Loging you in...\n')

        L.login(user,pwd)
        login = True
        Print('s', 'Login Sucess!')
    except:
        Print('d', 'Login Failed!')
        print()
        Print('w', 'Press Enter to Proceed without login...')
        input()

while True:
    clear_sc()
    banner()
    