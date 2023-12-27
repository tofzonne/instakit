import instaloader
from core.init import Print, info, banner, download, scanned
from instaloader.instaloadercontext import InstaloaderContext

context = InstaloaderContext()
ilogin = context.is_logged_in
L = instaloader.Instaloader()

banner()
Print('w', '\n1. Login to Instagram')
Print('w', '2. Without Login. Limited features\n\n\n')
opt = input('....../> ')
if opt == '1':
    banner()
    Print('i', 'To login enter the credentials')
    while not ilogin:
        username = input('\nUsername: ')
        try:
            instaloader.Instaloader.interactive_login(username)
            Print('s', 'Logged in successfully')
        except instaloader.exceptions.BadCredentialsException:
            banner()
            Print('w', 'Invalid credentials')
            Print('w', 'Try again')


def main():
    banner()
    Print('i', 'Scanning users...')
    while True:
        tar_user = input('\nTarget username: ')
        if tar_user == '':
            Print('w', 'No target username entered')
            continue
        banner()
        Print('i', f'Starting Scan on {tar_user}')
        print('`````````````````````````````````````````````````\n')
        try:
            profile = instaloader.Profile.from_username(L.context, tar_user)
            break
        except instaloader.exceptions.ConnectionException as e:
            Print('w', f'\n{tar_user} not found; "{e}"')
            Print('w', 'Check Spelling and Try again')
        except instaloader.exceptions.LoginRequiredException as r:
            Print('w', f'\nRedircted to login page; "{r}"')
            Print('d', 'Try again')
            exit()
    info(profile)
    download(profile)

while True:
    banner()
    print('\033[1;33ma: Scan users         b: See Scanned users        c: Exit\033[0m\n\n')
    opt = input('[>] Option: ')

    if opt.strip().lower()[0] == 'c':
        exit('\nGoodbye 👋')

    elif opt.strip().lower()[0] == 'b':
        scanned()

    else:
        main()