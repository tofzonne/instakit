import requests, os, platform

def banner():
    clear_sc()
    print("""
\033[1;32m
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗  ██╗██╗████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║ ██╔╝██║╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║█████╔╝ ██║   ██║   
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔═██╗ ██║   ██║   
██║██║ ╚████║███████║   ██║   ██║  ██║██║  ██╗██║   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   
            \033[0m""")

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
    message_type: The type of the message (warning, info, success, general).
    message: The message string to be printed.
  """
  colors = {
      "w": "\033[1;33m",
      "i": "\033[1;34m",
      "s": "\033[38;2;0;255;0m",
      "n": "\033[0m",
      "d": "\033[38;2;255;0;0m"
}
  symbols = {
      "w": "[!] ",
      "i": "[i] ",
      "s": "[+] ",
      "n": "[>] ",
      "d": "[*]"
  }

  color = colors.get(message_type.lower(), colors["n"])
  symbol = symbols.get(message_type.lower(), symbols["n"])

  print(f"{color}{symbol}{message}\033[0m")

def info(profile: object, login: bool = False):
    Print('s', f'Result: scan for {profile.full_name} on instagram\n')
    
    Print('i',f"Username: {profile.username}")
    Print('i',f"Full name: {profile.full_name}")
    Print('i',f"Biography: \n{profile.biography}")
    if profile.external_url:
        Print('i',f"Bio link: {profile.external_url}")
    Print('i',f"# Posts: {profile.mediacount}")
    Print('i',f"Followers: {profile.followers}")
    Print('i',f"Following: {profile.followees}")
    Print('i',f"Private account: {profile.is_private}")
    # Print('i', f'Is Professional Account: {profile}')
    Print('i',f"Verified account: {profile.is_verified}")
    if profile.is_business_account:
        Print('i',f"Is Business account: {profile.is_business_account}")
        Print('i',f"Business Category: {profile.business_category_name}")
    # Print('i',f"Story up: {profile.has_viewable_story}")
    if login:
        Print('i',"\nBlocking..............")
        Print('i',f"Blocked by followers: {profile.blocked_by_viewer}")
        Print('i',f"Blocked Viewer: {profile.has_blocked_viewer}")

        Print('i',"\nRequests............")
        Print('i',f"Viewer Request: {profile.requested_by_viewer}")
        Print('i',f"Reqest: {profile.has_requested_viewer}")

        count = 1
        for follower in profile.get_followers():
            print(f'{count}. {follower}')
            count += 1
            if count == 10:
                break

        count = 1
        for followee in profile.get_followees:
            print(f'{count}. {followee}')
            count += 1
            if count == 10:
                break
    
    askSave = input('\nDo you want to save the info? (Y/N) ')
    if askSave.strip().lower() == 'y':
        saveInfo(profile)

def saveInfo(profile: object):
    ...
    
def download(profile: object):
    user = f'{profile.username}_{profile.userid}_DP'
    name = profile.full_name
    # savedPosts = profile.get_saved_posts()

    os.makedirs(os.path.join(os.getcwd(), 'temp', name), exist_ok=True)
    dpdes = os.path.join(os.getcwd(), f'temp/{name}/{user}.jpg')
    downloadImg(profile.profile_pic_url, dpdes)

    download_post = False

    print('\n`````````````````````````````````````````````````\n')
    Print('s', 'Profile Picture Downloaded.')
    print('Do you want to download latest 5 posts of {0}?'.format(name))
    Print('w','Posts may include videos that might take time to download or crash the program')
    opt = input('...............(Y/N): ')
    if opt.strip().lower()[0] == 'y':
        download_post = True
        Print('i', f'Downloading Latest 5 posts of {profile.username}...\nFile path /temp/{profile.full_name}/Posts')

    if download_post:
        banner()
        posts = profile.get_posts()
        if posts:        
            os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'Posts'), exist_ok=True)
            count = 1
            for i in posts:
                # print(dir(i))
                # exit()
                if i.is_video:
                    postdes = os.path.join(os.getcwd(), f'temp/{name}/Posts/{name}_{count}.mp4')
                    downloadImg(i.video_url, postdes)
                else:
                    postdes = os.path.join(os.getcwd(), f'temp/{name}/Posts/{name}_{count}.jpg')
                    downloadImg(i.url, postdes)
                count += 1
                if count == 6:
                    break
        # if savedPosts:
        #     os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'Saved Posts'), exist_ok=True)
        #     count = 1
        #     for i in savedPosts:
        #         savePostDes = os.path.join(os.getcwd(), f'temp/{name}/Saved Posts/Saved_{name}_{count}.jpg')
        #         downloadImg(i.url, savedPosts)
        #         count += 1
        #         if count == 6:
        #             break

def downloadImg(url, destination):
        # print('Getting ur:')
        # print(url)
        response = requests.get(url)

        if response.status_code == 200:
            with open(destination, 'wb') as file:
                file.write(response.content)                
        else:
            Print('w', f"Failed to download image. Status code: {response.status_code}")