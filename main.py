import instaloader
from getpass import getpass
from core.init import Print, info, clear_sc, banner, download



login = False
L = instaloader.Instaloader()

banner()
Print('w', '1. Login')
Print('w', '2. Without Login...\n\n\n')
opt = input('....../> ')

if opt.strip()[0] == '1':
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
    banner()
    tar_user = input('\nTarget username: ')
    banner()
    Print('w', f'Starting Scan on {tar_user}')
    print('`````````````````````````````````````````````````\n')
    profile = instaloader.Profile.from_username(L.context, tar_user)
    info(profile, login)
    download(profile)