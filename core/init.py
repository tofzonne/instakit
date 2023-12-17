import requests
import os
import platform

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
  symbols = {
      "w": "[!] ",
      "i": "[i] ",
      "s": "[+] ",
      "n": "[>] ",
      "d": "[*] "
  }

  color = colors.get(message_type.lower(), colors["n"])
  symbol = symbols.get(message_type.lower(), symbols["n"])

  if message[0] == '\n':
      message = message[0].replace('\n', '')
      print(f'\n{color}{symbol}{message}\033[0m')

  print(f"{color}{symbol}{message}\033[0m")

def info(profile: object, login: bool = False):
    s = '\033[38;2;0;255;0m'
    e = '\033[0m'
    
    Print('s', f'Result: scan for {profile.full_name} on instagram\n')
    
    print(f'Username: {s}{profile.username}{e}')
    print(f'User ID: {s}{profile.userid}{e}')
    print(f'Full Name: {s}{profile.full_name}{e}')
    if profile.biography:
        print(f'Bio: \n{s}{profile.biography}{e}')
    if profile.external_url != None:
        print(f'Bio Link: {s}{profile.external_url}{e}')
    if profile.biography_mentions:
        for i , j in enumerate(profile.biography_mentions, j):
            print(f'Mention{j}: {s}{i.username}{e}')
    print(f'Followers: {s}{profile.followers}{e}')
    print(f'Following: {s}{profile.followees}{e}')
    print(f'Posts: {s}{profile.mediacount}{e}')
    try:
        print(f'Story up: {s}{profile.has_viewable_story}{e}')
    except ConnectionException as e:
        print(f'has_public_story: {s}{profile.has_public_story}{e}')
    print(f'Private Account: {s}{profile.is_private}{e}')
    print(f'Verified: {s}{profile.is_verified}{e}')
    if profile.is_business_account:
        print(f'Business Account: {s}{profile.is_business_account}{e}')
        if profile.business_category_name:
            print(f'Business Category: {s}{profile.business_category_name}{e}')
    
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
    getFile(profile.profile_pic_url, dpdes)

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
        print()
        Print('i', 'Downloading posts...')
        posts = profile.get_posts()
        if posts:        
            os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'Posts'), exist_ok=True)
            count = 1
            for i in posts:
                # print(dir(i))
                # exit()
                if i.is_video:
                    postdes = os.path.join(os.getcwd(), f'temp/{name}/Posts/{name}_{count}.mp4')
                    getFile(i.video_url, postdes)
                else:
                    postdes = os.path.join(os.getcwd(), f'temp/{name}/Posts/{name}_{count}.jpg')
                    getFile(i.url, postdes)
                count += 1
                if count == 6:
                    break
        # if savedPosts:
        #     os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'Saved Posts'), exist_ok=True)
        #     count = 1
        #     for i in savedPosts:
        #         savePostDes = os.path.join(os.getcwd(), f'temp/{name}/Saved Posts/Saved_{name}_{count}.jpg')
        #         getFile(i.url, savedPosts)
        #         count += 1
        #         if count == 6:
        #             break
        Print('s', f'{i} Posts Downloaded...')
        input('Press Enter to continue...')

def getFile(url, destination):
        # print('Getting ur:')
        # print(url)
        response = requests.get(url)

        if response.status_code == 200:
            with open(destination, 'wb') as file:
                file.write(response.content)                
        else:
            Print('w', f"Failed to download image. Status code: {response.status_code}")