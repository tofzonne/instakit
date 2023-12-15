import instaloader
from getpass import getpass
from core.init import Print, getimg, info, downloadPost, clear_sc, banner



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
    tar_user = input('\n\nTarget username: ')
    profile = instaloader.Profile.from_username(L.context, tar_user)
    getimg(profile.profile_pic_url, f'{profile.userid}_{profile.username}_DP')
    info(profile, login)
    downloadPost(profile)
    input('Press Enter to continue...')