import instaloader
from core.init import Print, info, clear_sc, banner, download, scanned


login = False
L = instaloader.Instaloader()

banner()
print()
Print('w', '1. Login')
Print('w', '2. Without Login...\n\n\n')
opt = input('....../> ')
if opt.strip()[0] == '1':
    banner()
    Print('i', 'To login enter the credentials')
    while login:
        username = input('\nUsername: ')
        try:
            instaloader.Instaloader.interactive_login(username)
            Print('s', 'Logged in successfully')
            login = True
        except instaloader.exceptions.BadCredentialsException:
            banner()
            Print('w', 'Invalid credentials')
            Print('w', 'Try again')
users = 0
while True:
    banner(users)
    print('\033[1;33ma: Scan users         b: See Scanned users        c: Exit\033[0m\n\n')
    opt = input('[>] Option: ')
    if opt.strip().lower()[0] == 'a':
        banner()
        Print('i', 'Scanning users...')
        tar_user = input('\nTarget username: ')
        banner(users)
        Print('i', f'Starting Scan on {tar_user}')
        print('`````````````````````````````````````````````````\n')
        try:
            profile = instaloader.Profile.from_username(L.context, tar_user)
        except instaloader.exceptions.ConnectionException as e:
            Print('w', f'{tar_user} not found "{e}"')
        info(profile, login)
        users += 1
        download(profile, login)

    elif opt.strip().lower()[0] == 'b':
        banner()
        scanned()

    else:
        exit('\nGoodbye 👋')
        