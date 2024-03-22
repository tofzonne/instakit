#!/usr/bin/env/python3
# Version: 1.3.0
from datetime import datetime
import instaloader
from core.init import *
from test import del_pycache_


L = instaloader.Instaloader()

def loadPrevSess(username):
    try:
        L.load_session_from_file(username)
        Print('s', 'Session loaded as %s' % L.test_login())
        input('Press enter to continue: ')
    except:
        Print('d', 'Fail to load Session! Press enter continue without login')
        input('\n:$ ')

def newLogin():
    banner()
    Print('i', '\nTo Login enter your credentials below')
    username = input('\nUsername: ')
    if username == '.b': return
    try:
        L.interactive_login(username)
        L.save_session_to_file()
        Print('s', '\nLogged in successfully')
        print('Press enter to Continue: ')
    except instaloader.exceptions.BadCredentialsException:
            banner()
            Print('d', 'Invalid credentials')
            Print('w', 'Try again')    

def main():
    banner()
    Print('i', 'Scanning users...')
    while True:
        tar_user = input('\nTarget username: ')
        if tar_user == '':
            Print('w', 'Username can\'t be empty')
            continue
        if tar_user == '.b': # ! Type `.b` if you accidentally selected Scan users to get out of loop.
            return
        banner()
        Print('i', f'\nStarting Scan on {tar_user}')
        print('`' * 48, '\n')
        stime = datetime.now()
        try:
            profile = instaloader.Profile.from_username(L.context, tar_user)
            break
        except instaloader.exceptions.ConnectionException as e:
            banner()
            Print('d', f'\n{e}')
            Print('w', 'Please Try again')
        except instaloader.exceptions.ProfileNotExistsException as e:
            banner()
            Print('d', f'\nUser "{tar_user}" does not Exists: {e}')
            Print('w', 'Check Spelling and Try again')
        except instaloader.exceptions.LoginRequiredException as r:
            banner()
            Print('w', f'\n{r}')
            Print('d', 'Try again or login first')
            exit()
        except instaloader.exceptions.QueryReturnedBadRequestException as b:
            banner()
            Print('d', f'\n{e}')
            
    # analyze(profile)
    elapsedTime(stime)
    info(profile)


if __name__ == '__main__':
    prevSession = showSessions()
    del_pycache_()
    if prevSession:
        banner()
        Print('s', f'\nYou\'ve {len(prevSession)} session.')
        print('`````````````````````````````````````````````````\n')
        for id, session in enumerate(prevSession, 1):
            print(f'      {id}. {session}')
        Print('s', '\nEnter the id to load session.')
        Print('s', 'Or 0 to login with new username.')
        option = int(input('\n:$ '))
        if option == 0:
            newLogin()

        elif option > 0:
            sessid = option - 1
            sessfile = prevSession[sessid]
            username = sessfile.replace('session-', '')
            loadPrevSess(username)
            
        else:
            pass # ! You can enter -1 or less values to skip to next step

    else:
        banner()
        Print('w', '\n1: Login to Instagram')
        Print('w', '2: Without login - limited features')
        opts = input('\n:$ ')
        if opts == '1':
            newLogin()

    while True:
        banner()
        print('\033[1;33ma: Scan users         b: See Scanned users        c: Exit\033[0m\n\n')
        opt : str = input(':$ ')
        
        if opt.strip().lower()[0] == 'c':
            exit('\nGoodbye 👋')
        
        elif opt.strip().lower()[0] == 'b':
            scanned()

        elif opt.strip() == 'analyze':
            from core.beta import Betamode
            asdf = Betamode()
            asdf._showVictims()
            # todo: Create a Brand New Function to hand the load
        
        else:
            main()