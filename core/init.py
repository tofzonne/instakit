from collections import Counter
import os
from pathlib import Path
import platform
from datetime import datetime
import json

import requests

from core.profile import UserProfile, followers, following, all_users, unique_users
from main import L

ilogin = L.context.is_logged_in

def banner() -> None:
    """
    Clears the Screen and Prints the banner
    """
    clear_sc()

    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    flname = os.path.join(os.getcwd(), "core", "logs", "info.log")

    logs_path = Path(flname)
    if logs_path.exists():
        logs = logs_path.read_text().splitlines()
    else:
        logs = []

    today = now.strftime("%d-%m-%y")
    tcount = sum(1 for line in logs if datetime.strptime(line.split(',')[1].strip(), '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%y') == today)
    srno = "" if tcount == 0 else f"Scanned today: {tcount}/{len(logs)} users"

    if ilogin:
        bann = f"\033[0mLogged in as:\033[92m {L.test_login()}\033[0m"
    else:
        bann = ""
    print(f"""
Time: {time}                    {srno}\033[92m 
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗  ██╗██╗████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║ ██╔╝██║╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║█████╔╝ ██║   ██║   {bann}
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔═██╗ ██║   ██║
██║██║ ╚████║███████║   ██║   ██║  ██║██║  ██╗██║   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝\033[0m""")

def clear_sc():
    """
    Clears the screen.
    """
    sys_os = platform.system()
    if sys_os == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def Print(msg_type: str, msg: str) -> None:
    """
    Prints a message to the console with color and symbol formatting based on message type.

    Args:
        `msg_type`: A string representing the message type, used for formatting.
        Valid options are:
            `w` -> warning,
            `i` -> info,
            `n` -> normal,
            `d` -> danger, or
            `s` -> success.
        `msg`: The message to be printed.
    """
    colors = {
            "w": "\033[1;33m",
            "i": "\033[1;34m",
            "s": "\033[38;2;0;255;0m",
            "n": "\033[0m",
            "d": "\033[38;2;255;0;0m"
    }
    symbols = {"w": "[!] ", "i": "[i] ", "s": "[+] ", "n": "[>] ", "d": "[*] "}

    color = colors.get(msg_type.lower(), colors["n"])
    symbol = symbols.get(msg_type.lower(), symbols["n"])

    if '\n' in msg[0]:
        msg = msg.replace('\n', '')
        print(f'\n{color}{symbol}{msg}\033[0m')
    else:
        print(f"{color}{symbol}{msg}\033[0m")

def log(username: str, userid: int):
    """
    Logs a user's activity to a file named `info.log` in the `core/logs` directory.

    Args:
        `username`: The username of the user to log.
        `userid`: The user's ID.
    """
    os.makedirs(os.path.join(os.getcwd(), "core", "logs"), exist_ok=True)
    flname = os.path.join(os.getcwd(), "core", "logs", "info.log")
    with open(flname, 'a') as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{username}, {time}, {userid}\n")

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
        opt = input('\n:$ ')
        if opt == 'a':
            banner()
            all_users(user)
        else:
            banner()
            unique_users(user)
        # sleep(1)
        opt = input('\n\n:$ ')
        if opt == 'c':
            os.remove(flname)
            Print('s','Log cleared')

def info(profile: object):
    s = '\033[38;2;0;255;0m'
    e = '\033[0m'
    meta = profile._metadata
    data = UserProfile(meta)
    log(data.username, data.id)

    if len(data.full_name) < 1:
        fname = "['Name']"
    else:
        fname = data.full_name

    Print('s', f'Results: scan for {fname} on instagram')

    print(f'User Id: {s}{data.id}{e}')
    print(f'Username: {s}{data.username}{e}')
    print(f'Full Name: {s}{data.full_name}{e}')

    pronoun = data.pronouns
    if len(pronoun) != 0:
        print(f'Pronouns: {s}', end='')
        for i in pronoun:
            print(i.title(), end=', ')
        print(e)

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

    print(f'Total Media: {s}{profile.mediacount}{e}')
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

    print(f'Supervision Enabled: {s}{data.is_supervision_enabled}{e}')

    print(f'Supervised by someone: {s}{data.is_supervised_user}{e}')

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
            # ! Check '.has_blocked_viewer' function on instaloader module

    if data.has_guides:
        print(f'{data.full_name} has Guides: {s}{data.has_guides}{e}')

    if ilogin and data.mutual_followed_by is not None:
        print(f'You\'ve mutual followers with {s}{data.full_name}{e}')
        # TODO Write logic to print username's of mutual followers

    if ilogin:
        ers = followers(profile)
        ees = following(profile)
        print('`````````````````````````````````````````````````\n')
        print(f'Top ten Followers of {s}{data.username}{e}')
        for x in range(1, 10):
            print(f'{x}: ', ers[x-1]['username'], ers[x-1]['full_name'])

        print('`````````````````````````````````````````````````\n')
        print(f'Top ten Following of {s}{data.username}{e}')
        for x in range(1, 10):
            print(f'{x}: ', ees[x-1]['username'], ees[x-1]['full_name'])

    beta = Data(data, profile.mediacount)
    if beta:
        saveInfo(profile)
        analyze(profile)
    else:
        askSave = input('\nSave these info? (y/n):$ ')
        if askSave.strip().lower() == 'y':
            saveInfo(profile)

def saveInfo(profile: object):
    name = f'{profile.username}_{profile.userid}'
    meta = profile._metadata
    data = UserProfile(meta)
    time = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'data'), exist_ok=True)
    flname = os.path.join(os.getcwd(), "temp", name, "data", f"{profile.username}.txt")

    with open(flname, 'w', encoding='utf-8') as f:
        if ilogin:
            f.write(f'You\'wre logged in as {L.test_login()}\n')
        f.write(f'Scan at: {time}\n')
        f.write(f'User Id: {profile.userid}\n')
        f.write(f'Username: {profile.username}\n')
        f.write(f'Full Name: {profile.full_name}\n')
        f.write(f'Prnouns: {data.pronouns}\n')
        f.write(f'Bio: {profile.biography}\n{profile.external_url}\n')
        f.write(f'Join recently: {data.is_joined_recently}\n')
        f.write(f'Followers: {data.followers}\n')
        f.write(f'Following: {data.followees}\n')
        f.write(f'Total Media: {profile.mediacount}\n')
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
            Print('s', 'Followers data Saved.')
        with open(sdes, 'w') as f:
            json.dump(followee, f, indent=4)
            Print('s', 'Followings data Saved.')

    banner()
    Print('s', f'Saved info for {profile.full_name} to temp/{name}/data/')

def download(profile: object):
    """
    Downloads profile picture and optionally the latest `#` of posts from an Instagram profile.

    Args:
        `profile`: An instaloader.Profile object representing the target Instagram profile.

    Raises:
        `LoginRequiredExeption`: If the profile is private or You're not logged in.

    """
    name = f'{profile.username}_{profile.userid}'
    dpUrl = profile.profile_pic_url

    os.makedirs(os.path.join(os.getcwd(), 'temp', name), exist_ok=True)
    dpdes = os.path.join(os.getcwd(), f'temp/{name}/DP-{profile.username}.jpg')
    getFile(dpUrl, dpdes) # * Downloads Profile picture of target username
    print('`````````````````````````````````````````````````\n')
    Print('s', 'Profile Picture Downloaded.')

    download_post = False

    num_posts = profile.mediacount
    if num_posts <= 0:
        Print('i', f'\nNo posts found for {profile.username}. Press enter to continue.')
        # input('\n:$ ')

    elif profile.is_private and not ilogin:
        Print('w', f"\n{profile.username} has {num_posts} posts, but it's private.")
        Print('d', "Can't download posts of private accounts.")
        Print('d', f"Unless you log in and follow {profile.username}\n")
    
    else:  
        Print('w', f"Enter # of posts to Download form {profile.username}. Else 0.")
        Print('d', f'Max #: {min(num_posts, 50)}')
        opt = input("\n: [int]$ ")

        if not opt == "0":
            Print('i', f"Downloading latest {opt} posts of {profile.username}...")
            Print('i', f"File path: /temp/{name}/Posts/")
            download_post = True

    if download_post:
        banner()
        posts = profile.get_posts()
        os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'Posts'), exist_ok = True)
        Print('i', '\nDownloading posts...')
        for count, i in enumerate(posts, 1):
            flname = i.pcaption
            rep = """<>?/:"'|*"""
            for x in rep:
                flname = flname.replace(x, '_')
            if i.is_video:
                url = i.video_url
                postdes = os.path.join(
                        os.getcwd(), f'temp/{name}/Posts/{count}-{flname}.mp4')
                ex = '.mp4'
            else:
                url = i.url
                postdes = os.path.join(
                        os.getcwd(), f'temp/{name}/Posts/{count}-{flname}.jpg')
                ex = '.jpg'

            getFile(url, postdes) # * Downloads each posts of target usrname till given number

            Print('s', f"{count}-{flname}        '({ex})' Downloaded...")
            if count == int(opt):
                break

    input('Press Enter to continue...')

def getFile(url: str, destination: str) -> None:
    """
    Downloads a file from a given URL and saves it to the specified destination.

    Args:
        `url`: The URL of the file to download.
        `destination`: The path to save the downloaded file to.

    Raises:
        `RuntimeError`: If the download fails with a non-`200` status code.
        
    """
    response = requests.get(url)

    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
    else:
        Print('w',
                    f"Failed to download file. Status code: {response.status_code}")

def elapsedTime(StartingTime) -> str:
    """
    Calculates the elapsed time in seconds between the current time and a given starting time.

    Args:
        `StartingTime`: A datetime object representing the starting time.

    Returns:
        A string representing the elapsed time in `seconds`, rounded to two decimal places.
    """
    etime = datetime.now()
    elapsed_time = etime - StartingTime
    seconds = int(elapsed_time.total_seconds())
    Print('i', f'Scan completed in {round(seconds, 2)} seconds\n')

def showSessions() -> list[str] | bool:
    """
    Attempts to retrieve a list of saved Instaloader sessions.

    Returns:
        A list of session file names if sessions are found, otherwise False.
    """
    from instaloader.instaloader import _get_config_dir
    directory = _get_config_dir()
    try:
        files = os.listdir(directory)
        return files
    except FileNotFoundError:
        return False

def getPostDict(rawposts) -> dict:
    posts = {}
    for count, i in enumerate(rawposts, 1):
        if count == 100: break
        posts[i.shortcode] = {
            'likes': i.likes,
            'comments': i.comments,
            'caption': i.caption,
            'hastags': i.caption_hashtags,
            'date': i.date
        }
    return posts

def Data(info: object, media: int):
    folder = os.path.join(os.getcwd(), 'core', 'logs', '.Poeples')
    os.makedirs(folder, exist_ok = True)
    quoted_folder_path = f'"{os.path.abspath(folder)}"'
    os.system(f'attrib +h {quoted_folder_path}')
    filename = folder + f'/{info.id}.json'
    
    today = datetime.now().strftime("%Y-%m-%d")
    okey = False
    try:
        with open(filename) as f:
            database = json.load(f)
        if len(database) > 2: # * change the thresold if needed
            okey = True
    except:
        database = {}
    
    database[today] = {
        'userId': info.id,
        'username': info.username,
        'name': info.full_name,
        'recently join': info.is_joined_recently,
        'bio': info.biography,
        'externalLink': info.external_url,
        'follower': info.followers,
        'followee': info.followees,
        'media': media,
        'private': info.is_private,
        'verified': info.is_verified,
        'professional': {
            'status': info.is_professional_account,
            'category': info.category_name},
        'business': {
            'status': info.is_business_account,
            'category': info.business_category_name,
            'email': info.business_email,
            'phone': info.business_phone},
        'pronouns': info.pronouns,
        'guides': info.has_guides
    }
    
    with open(filename, 'w') as f:
        json.dump(database, f, indent=2)
    
    if okey:
        Print('i', '\nYou\'ve enough information to generate a detailed report of {}.'.format(info.username))
        que = input('Do you want to analyze this profile [y/n] :$ ')
        if que[0].lower() == 'y':
            return True

def analyze(profile: object):
    """
    """
    rawposts = profile.get_posts()
    posts = getPostDict(rawposts)
    topcapword = topword(posts)
    tophashtag = tophash(posts)

    engag, acti = engagement(profile, posts)
    popularDay, popularTime = schedule(posts)

    print(f'Engagement: {engag}%\n\nUser Activity: {acti}%\n')
    print(f'uploads: {profile.mediacount}\n')
    print('Top cap word:')
    for word, occr in topcapword.items():
        print(f'{word}: {occr}')
    print('\nTop hashtag:')
    for hash, occr in tophashtag.items():
        print(f'{hash}: {occr}')
    print(f'\nPopular day: {popularDay}\n')
    print(f'Popular time: {popularTime}\n')

def topword(dictionary: dict) -> dict:
    """
    Finds the most frequent words in captions, excluding stop words and irrelevant characters.

    Args:
        dictionary: A dictionary containing post IDs and their captions.

    Returns:
        A dictionary containing the most frequent words and their counts, sorted in descending order by count.
    """

    captions = [post.get('caption', '') for post_id, post in dictionary.items()]

    stop_words = set(open('core/filler.txt').read().splitlines())

    valid_words = Counter(
        word.lower() for caption in captions if caption != None for word in caption.split()
        if word.isalnum() and word.lower() not in stop_words and '#' not in word
    )

    return dict(valid_words.most_common())

def tophash(dictionary: dict) -> dict:
    """
    """
    has = [post['hastags'] for post_id, post in dictionary.items()]
    words = {}
    for a in range(len(has)):
        for i in has[a]:
            words[i] = words.get(i, 0) + 1
    sort_words = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))
    return sort_words

def engagement(profile, posts_dict):
    follower_count = profile.followers
    total_likes = sum(post['likes'] for post_id, post in posts_dict.items())
    total_comments = sum(post['comments'] for post_id, post in posts_dict.items())
    total_engagement = total_likes + total_comments
    engagement_rate = (total_engagement / follower_count) * 100

    activity = (total_comments + total_likes + profile.mediacount) / profile.followers

    return round(engagement_rate,2), round(activity,2)

def schedule(posts_dict):
    posting_days = [post['date'].strftime('%A') for _, post in posts_dict.items()]
    posting_times = [post['date'].strftime('%H:%M:%S') for _, post in posts_dict.items()]

    popular_day = max(set(posting_days), key=posting_days.count)
    popular_time = max(set(posting_times), key=posting_times.count)

    return popular_day, popular_time