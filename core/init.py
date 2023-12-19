import requests
import os
import platform
from instaloader.exceptions import ConnectionException
from core.profile import UserProfile

def banner():
    clear_sc()
    print(f"""\033[92m

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
    meta = profile._metadata
    data = UserProfile(meta)
    
    Print('s', f'Result: scan for {data.full_name} on instagram\n')

    print(f'User Id: {s}{data.id}{e}')
    print(f'Username: {s}{data.username}{e}')
    print(f'Full Name: {s}{data.full_name}{e}')
    print(f'Followers: {s}{data.followers}{e}')
    print(f'Followees: {s}{data.followees}{e}')
    if len(data.biography) > 2 and data.external_url != None:
        print(f'Bio: \n{s}{data.biography}\n{data.external_url}{e}')
    elif len(data.biography):
        print(f'Bio: \n{s}{data.biography}{e}')
    print(f'Private: {s}{data.is_private}{e}')
    print(f'Verified: {s}{data.is_verified}{e}')
    print(f'Professional: {s}{data.is_professional_account}{e}')
    if data.category_name != None:
        print(f'Category: {s}{data.category_name}{e}')
    if data.is_business_account:
        print(f'Business Account: {s}{data.is_business_account}{e}')
        if data.business_category_name != None:
            print(f'Business Category: {s}{data.business_category_name}{e}')
        if data.business_email != None:
            print(f'BussinessEmail: {s}{data.business_email}{e}')
        if data.business_phone != None:
            print(f'Business Phone #: {s}{data.business_phone}{e}')
    
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
    if not profile.is_private:
        print('Do you want to download latest 5 posts of {0}?'.format(name))
        Print('w','Posts may include videos that might take time to download or crash the program')
        opt = input('...............(Y/N): ')
        if opt.strip().lower()[0] == 'y':
            download_post = True
            Print('i', f'Downloading Latest 5 posts of {profile.username}...\nFile path /temp/{profile.full_name}/Posts')
    else:
        u = profile.get_posts().count
        Print("w", f"\n{profile.username} has {u} can't download posts because it's private.")
        input('Press Enter to continue...')

    if download_post:
        banner()
        print()
        Print('i', 'Downloading posts...')
        posts = profile.get_posts()
        if posts:        
            os.makedirs(os.path.join(os.getcwd(), 'temp', name, 'Posts'), exist_ok=True)
            
            for count, i in enumerate(posts,1):
                # print(dir(i))
                # exit()
                if i.is_video:
                    postdes = os.path.join(os.getcwd(), f'temp/{name}/Posts/{count}_{i.pcaption}.mp4')
                    getFile(i.video_url, postdes)
                else:
                    postdes = os.path.join(os.getcwd(), f'temp/{name}/Posts/{count}_{i.pcaption}.jpg')
                    getFile(i.url, postdes)
                if count == 5:
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
            Print('s', f'{count} Posts Downloaded...')
        else:
            Print('w', f'No posts found for {profile.username}.')
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