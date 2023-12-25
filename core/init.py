import os
import platform
from datetime import datetime
import json
from time import sleep

import requests
from instaloader.instaloadercontext import InstaloaderContext

from core.profile import UserProfile, followers, following, all, unique_users

context = InstaloaderContext()
ilogin = context.is_logged_in


def banner(): 
    clear_sc()
    time = datetime.now().strftime("%H:%M:%S")
    flname = os.path.join(os.getcwd(), "core", "logs", "info.log")
    try:
        with open(flname, 'r') as f:
            logs =  f.readlines()
    except FileNotFoundError:
        logs = []
    today = datetime.now().strftime("%d-%m-%y")
    count = len(logs)
    tcount = 0
    for i in logs:
        raw = i.split(',')[1].strip()
        Time = datetime.strptime(raw, '%Y-%m-%d %H:%M:%S')
        day = Time.strftime('%d-%m-%y')
        if today == day:
            tcount += 1
    srno = "" if tcount == 0 else f"Scanned today: {tcount}/{count} users"
    print(f"""
Time: {time}                    {srno}\033[92m 
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗  ██╗██╗████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║ ██╔╝██║╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║█████╔╝ ██║   ██║   
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔═██╗ ██║   ██║   
██║██║ ╚████║███████║   ██║   ██║  ██║██║  ██╗██║   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝\033[0m""")

def clear_sc():
    sys_os = platform.system()
    if sys_os == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def Print(message_type: str, message: str):
    """
    Prints a message with color and symbol based on its type.

    Args:
        message_type: The type of the message (w, i, s, n, d).
        message: The message string to be printed.
    """
    colors = {
            "w": "\033[1;33m",
            "i": "\033[1;34m",
            "s": "\033[38;2;0;255;0m",
            "n": "\033[0m",
            "d": "\033[38;2;255;0;0m"
    }
    symbols = {"w": "[!] ", "i": "[i] ", "s": "[+] ", "n": "[>] ", "d": "[*] "}

    color = colors.get(message_type.lower(), colors["n"])
    symbol = symbols.get(message_type.lower(), symbols["n"])

    if '\n' in message[0]:
        message = message.replace('\n', '')
        print(f'\n{color}{symbol}{message}\033[0m')
    else:
        print(f"{color}{symbol}{message}\033[0m")

def log(message: str):
    os.makedirs(os.path.join(os.getcwd(), "core", "logs"), exist_ok=True)
    flname = os.path.join(os.getcwd(), "core", "logs", "info.log")
    with open(flname, 'a') as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{message}, {time}\n")

def scanned():
    flname = os.path.join(os.getcwd(), "core", "logs", "info.log")
    try:
        with open(flname) as f:
            user =  f.readlines()
    except FileNotFoundError:
        user = []
    banner()
    if len(user) == 0:
        Print('w', '\nYou have not scanned any users yet')
        Print('i', 'Press enter to continue...\n')
        input()
    else:
        Print('i', '\na: View all scanned users')
        Print('i', 'u: View Unique Scanned users')
        opt = input('\nChoose an option: ')
        if opt == 'a':
            all(user)
        else:
            unique_users(user)
        # sleep(1)
        print('|   c: Clear Log{: ^20}q: Quit   |'.format('|'))
        print('+------------------------+--------------------+\n')
        opt = input('\n\n[>] Choose an option: ')
        if opt == 'c':
            os.remove(flname)
            print('Log cleared')

def info(profile: object):
    s = '\033[38;2;0;255;0m'
    e = '\033[0m'
    meta = profile._metadata
    data = UserProfile(meta)
    log(data.username)

    Print('s', f'Results: scan for {data.full_name} on instagram')

    print(f'User Id: {s}{data.id}{e}')
    print(f'Username: {s}{data.username}{e}')
    print(f'Full Name: {s}{data.full_name}{e}')

    pronoun = data.pronouns
    if len(pronoun) != 0:
        print(f'Pronouns: {s}', end='')
        for i in pronoun:
            print(i.title(), end=', ')
        print(e)

    if data.is_joined_recently:
        print(f'Joined Recently: {s}{data.is_joined_recently}{e}')

    print(f'Followers: {s}{data.followers}{e}')
    print(f'Following: {s}{data.followees}{e}')

    if len(data.biography) > 2 and data.external_url is not None:
        print(f'Bio: \n{s}{data.biography}\n{data.external_url}{e}')

    elif len(data.biography) > 1:
        print(f'Bio: \n{s}{data.biography}{e}')
    
    if ilogin and profile.followed_by_viewer:
        print(f'You\'re following {s}{data.username}{e}.')

    if ilogin and profile.follows_viewer:
        print(f'{s}{data.username}{e} follows you.')

    if ilogin and profile.has_requested_viewer:
        print(f'{s}{data.username}{e} requested you.')

    if ilogin and profile.requested_by_viewer:
        print(f'You\'re requesting {s}{data.username}{e}.')

    print(f'Total Media: {s}{profile.get_posts().count}{e}')
    print(f'Private: {s}{data.is_private}{e}')
    print(f'Verified: {s}{data.is_verified}{e}')
    print(f'Professional: {s}{data.is_professional_account}{e}')

    if data.category_name is not None:
        print(f'Category: {s}{data.category_name}{e}')

    if data.is_business_account:
        print(f'Business Account: {s}{data.is_business_account}{e}')
        if data.business_category_name is not None:
            print(f'Business Category: {s}{data.business_category_name}{e}')
        if data.business_email is not None:
            print(f'BussinessEmail: {s}{data.business_email}{e}')
        if data.business_phone is not None:
            print(f'Business Phone #: {s}{data.business_phone}{e}')

    if data.is_supervision_enabled:
        print(f'Supervision Enabled: {s}{data.is_supervision_enabled}{e}')

    if data.is_supervised_user:
        print(f'Supervisied by someone: {s}{data.is_supervised_user}{e}')

    if ilogin:
        if data.is_supervised_by_viewer:
            print(f'You\'re Supervising {s}{data.full_name}{e}.')
        if data.is_guardian_of_viewer:
            print(f'You\'re being Supervisied by {s}{data.full_name}{e}')
        if data.guardian_id is not None:
            print(f'Guardian Id: {s}{data.guardian_id}{e}')
        if data.blocked_by_viewer:
            print(f'You\'ve blocked {s}{data.full_name}{e}.')
        if data.restricted_by_viewer:
            print(f'You\'ve Restricted {s}{data.full_name}{e}.')
        if profile.has_blocked_viewer:
            print(f'{s}{data.full_name}{e} has blocked you.')

    if data.has_guides:
        print(f'{data.full_name} has Guides: {s}{data.has_guides}{e}')

    if ilogin and data.mutual_followed_by is not None:
        print(f'You\'ve mutual followers with {s}{data.full_name}{e}')
        # for profile:]

    if ilogin:
        ers = followers(profile)
        ees = following(profile)
        print('`````````````````````````````````````````````````\n')
        print(f'Top ten Followers of {s}{data.username}{e}')
        for x in range(1, 10):
            print(f'{x}: ', ers[x]['username'], ers[x]['full_name'])

        print('`````````````````````````````````````````````````\n')
        print(f'Top ten Following of {s}{data.username}{e}')
        for x in range(1, 10):
            print(f'{x}: ', ees[x]['username'], ees[x]['full_name'])


    askSave = input('\nDo you want to save the info? (Y/N) ')
    if askSave.strip().lower() == 'y':
        saveInfo(profile)

def saveInfo(profile: object):
    name = f'{profile.username}_{profile.userid}'
    meta = profile._metadata
    data = UserProfile(meta)

    os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'data'), exist_ok=True)
    flname = os.path.join(os.getcwd(), "temp", name, "data", f"{profile.username}.txt")

    with open(flname, 'w', encoding='utf-8') as f:
        time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        if ilogin:
            f.write('You\'wre logged in\n')
        f.write(f'Scan at {time}\n')
        f.write(f'User Id: {profile.userid}\n')
        f.write(f'Username: {profile.username}\n')
        f.write(f'Full Name: {profile.full_name}\n')
        f.write(f'Prnouns: {data.pronouns}\n')
        f.write(f'Bio: {profile.biography}\n{profile.external_url}\n')
        f.write(f'Join recently: {data.is_joined_recently}\n')
        f.write(f'Followers: {data.followers}\n')
        f.write(f'Following: {data.followees}\n')
        f.write(f'Total Media: {profile.get_posts().count}\n')
        f.write(f'Private: {data.is_private}\n')
        f.write(f'Verified: {data.is_verified}\n')
        f.write(f'Professional: {data.is_professional_account}\n')
        f.write(f'Category: {data.category_name}\n')
        f.write(f'Business Account: {data.is_business_account}\n')
        f.write(f'Business Category: {data.business_category_name}\n')
        if ilogin:
            if profile.followed_by_viewer:
                f.write(f'You\'re following {data.username}\n')
            if data.is_supervised_user:
                f.write(f'{data.username} is Supervised by Some other user\n')
            if profile.follows_viewer:
                f.write(f'{data.username} follows you\n')
            if profile.has_requested_viewer:
                f.write(f'{data.username} requested you\n')
            if profile.requested_by_viewer:
                f.write(f'You\'re requesting {data.username}\n')
            if profile.has_blocked_viewer:
                f.write(f'{data.username} has blocked you\n')
            if data.restricted_by_viewer:
                f.write(f'You\'ve Restricted {data.username}\n')
            if data.blocked_by_viewer:
                f.write(f'You\'ve blocked {data.username}\n')
            if data.is_supervised_by_viewer:
                f.write(f'You\'re Supervising {data.username}\n')
        f.write(f'{data.username} has Guides: {data.has_guides}\n')
        f.write(f'Guardian Id: {data.guardian_id}\n')            

    
    if ilogin:
        rdes = os.path.join(os.getcwd(), "temp", name, "data", "followers.txt")
        sdes = os.path.join(os.getcwd(), "temp", name, "data", "followings.txt")
        follower = followers(profile)
        followee = following(profile)
        with open(rdes, 'w') as f:
            json.dump(follower, f, indent=4)
            Print('s', 'Followers data')
        with open(sdes, 'w') as f:
            json.dump(followee, f, indent=4)
            Print('s', 'Followings data')

    banner()
    Print('s', f'Saved info for {profile.full_name} to temp/{name}/data/')

def download(profile: object):
    """
    Downloads profile picture and optionally the latest 5 posts from an Instagram profile.

    Args:
        profile: An instaloader.Profile object representing the target Instagram profile.
        login: A boolean indicating whether to use a logged-in Instaloader session for private accounts.
                Defaults to False.

    Raises:
        LoginRequiredExeption: If the profile is private and login is False.

    """
    name = f'{profile.username}_{profile.userid}'
    dpUrl = profile.profile_pic_url

    os.makedirs(os.path.join(os.getcwd(), 'temp', name), exist_ok=True)
    dpdes = os.path.join(os.getcwd(), f'temp/{name}/DP-{profile.username}.jpg')
    getFile(dpUrl, dpdes)

    download_post = False

    print('`````````````````````````````````````````````````\n')
    Print('s', 'Profile Picture Downloaded.')
    if profile.is_private and not ilogin:
        u = profile.get_posts().count
        Print('w', '{0} has {1} posts but its private.\n'.format(profile.username, u))
        Print('d', 'Can\'t download posts of private accounts.')
        Print('d', f'Unless you login and Follow {profile.username}\n.')
        input('Press Enter to continue...')
    else:
        print('Do you want to download latest 5 posts of {0}?'.format(
                profile.username))
        # Print('w','Posts may contain videos that may take a time to download. \n')
        opt = input('\nContinue (Y/N): ')
        
        if opt.strip().lower()[0] == 'y':
            download_post = True
            Print('i', f'Downloading Latest 5 posts of {profile.username}...')
            Print('i', f'File path /temp/{name}/Posts')

    if download_post:
        banner()
        print()
        posts = profile.get_posts()
        if posts.count > 0:
            os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'Posts'), exist_ok = True)
            Print('i', 'Downloading posts...')
            for count, i in enumerate(posts, 1):
                flname = i.pcaption
                rep = """<>?/:"|*"""
                for x in rep:
                    flname = flname.replace(x, '_')
                if i.is_video:
                    postdes = os.path.join(
                            os.getcwd(), f'temp/{name}/Posts/{count}-{flname}.mp4')
                    getFile(i.video_url, postdes)
                else:
                    postdes = os.path.join(
                            os.getcwd(), f'temp/{name}/Posts/{count}-{flname}.jpg')
                    getFile(i.url, postdes)
                Print('s', f'{count}-{flname} Downloaded...')
                if count == 5:
                    break
        else:
            Print('w', f'No posts found for {profile.username}.')

        input('Press Enter to continue...')

def getFile(url, destination):
    """
    Downloads a file from a given URL and saves it to the specified destination.

    Args:
        `url`: The URL of the file to download.
        `destination`: The path to save the downloaded file to.

    Raises:
        `RuntimeError`: If the download fails with a non-200 status code.
        
    """
    response = requests.get(url)

    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
    else:
        Print('w',
                    f"Failed to download file. Status code: {response.status_code}")
