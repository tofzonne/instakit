#!/usr/bin/env/python3
# Version: 1.1
from datetime import datetime
import instaloader
from core.init import *


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
    Print('w', '\n1: Login to Instagram')
    Print('w', '2: Without login - limited features')
    opt = input('\n:$ ')
    if opt == '1':
        banner()
        Print('i', '\nTo Login enter your credentials below')
        username = input('\nUsername: ')
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
        print('`````````````````````````````````````````````````\n')
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
            
    Print('i', f'Scan completed in {elapsedTime(stime)} seconds\n')
    info(profile)
    download(profile)


if __name__ == '__main__':
    prevSession = showSessions()
    if prevSession:
        banner()
        Print('s', f'\nYou\'ve {len(prevSession)} session.')
        print('`````````````````````````````````````````````````\n')
        for id, session in enumerate(prevSession, 1):
            print(f'      {id}. {session}')
        Print('s', '\nEnter the id to load session.')
        Print('s', 'Or 0 to login with new username.')
        opt = int(input('\n:$ '))
        if opt == 0:
            banner()
            Print('i', '\nTo Login enter your credentials below.')
            username = input('\nUsername: ')
            try:
                L.interactive_login(username)
                L.save_session_to_file()
                Print('s', '\nLogged in successfully')
            
            # except instaloader.exceptions.BadCredentialsException: # default
            except Exception as e: #! test
                banner()
                Print('d', e)
                Print('d', 'Invalid credentials')
                Print('w', 'Try again')
                input(':\\n ')

        elif opt > 0:
            sessid = opt - 1
            sessfile = prevSession[sessid]
            username = sessfile.replace('session-', '')
            # print('usernaem', username, len(username))
            loadPrevSess(username)
            
        else:
            pass

    else:
        newLogin()
    while True:
        banner()
        print('\033[1;33ma: Scan users         b: See Scanned users        c: Exit\033[0m\n\n')
        opt = input(':$ ')
        
        if opt.strip().lower()[0] == 'c':
            exit('\nGoodbye 👋')
        
        elif opt.strip().lower()[0] == 'b':
            scanned()
        
        else:
            main()