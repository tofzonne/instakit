import requests, os, platform

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

def getimg(url, imgName: str, folder: str = 'Profile_pic'):
    response = requests.get(url)

    temp = os.path.join(os.getcwd(), f'temp/{folder}')
    if not os.path.exists(temp):
        os.makedirs(temp)
    destination = os.path.join(temp, f'{imgName}.jpg')


    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        # Print('s', 'Pic Download Successfull')
    else:
        Print('w', f"Failed to download image. Status code: {response.status_code}")

def downloadPost(profile: object):
    posts = profile.get_posts()
    count = 1
        
    for i, post in enumerate(posts,1):
        getimg(post.url,f'{profile.username}_{count}',f'Posts_{profile.full_name}')
        count += 1
        if count == 5:
            break

def info(Profile: object):

    Print('i', f"{profile.full_name}'s info...\n")
    
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
        profile
    Print('i',f"Story up: {profile.has_viewable_story}")
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

    
