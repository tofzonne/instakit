import instaloader
from core.init import Print, info, clear_sc, banner, download


login = False
L = instaloader.Instaloader()

banner()
Print('w', '1. Login')
Print('w', '2. Without Login...\n\n\n')
opt = input('....../> ')
if opt.strip()[0] == '1':
    banner()
    Print('i', 'To login enter the credentials')
    username = input('\nUsername: ')
    try:
        instaloader.Instaloader.interactive_login(username)
        Print('s', 'Logged in successfully')
    except:
        banner()
        Print('w', 'Invalid credentials')

while True:
    banner()
    tar_user = input('\nTarget username: ')
    banner()
    Print('w', f'Starting Scan on {tar_user}')
    print('`````````````````````````````````````````````````\n')
    profile = instaloader.Profile.from_username(L.context, tar_user)
    info(profile, login)
    download(profile)