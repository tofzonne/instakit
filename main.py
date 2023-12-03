import instaloader, os, sys

def banner():
        print("""
'####:'##::: ##::'######::'########::::'###:::::::::::::'##:::'##:'####:'########:
. ##:: ###:: ##:'##... ##:... ##..::::'## ##:::::::::::: ##::'##::. ##::... ##..::
: ##:: ####: ##: ##:::..::::: ##:::::'##:. ##::::::::::: ##:'##:::: ##::::: ##::::
: ##:: ## ## ##:. ######::::: ##::::'##:::. ##:'#######: #####::::: ##::::: ##::::
: ##:: ##. ####::..... ##:::: ##:::: #########:........: ##. ##:::: ##::::: ##::::
: ##:: ##:. ###:'##::: ##:::: ##:::: ##.... ##:::::::::: ##:. ##::: ##::::: ##::::
'####: ##::. ##:. ######::::: ##:::: ##:::: ##:::::::::: ##::. ##:'####:::: ##::::
....::..::::..:::......::::::..:::::..:::::..:::::::::::..::::..::....:::::..:::::""")


# Instaloader Configuration
L = instaloader.Instaloader()

banner()
username = input('\nTarget username: ')
if username == '':
  print(f'{os.path.basename(__file__)}: username cannot be empty')
  sys.exit(1)

profile = instaloader.Profile.from_username(L.context, username)
os.system('clear')
banner()
print(f"\nExtracting {profile.full_name}'s info...\n")
print(f"Username: {profile.username}")
print(f"Full name: {profile.full_name}")
print(f"Biography: {profile.biography}")
print(f"Bio link: {profile.external_url}")
print(f"# Posts: {profile.mediacount}")
print(f"Followers: {profile.followers}")
print(f"Following: {profile.followees}")
# print(f"Profile pic url: {profile.profile_pic_url}")
print(f"Private account: {profile.is_private}")
print(f"Verified account: {profile.is_verified}")
print(f"Is Business account: {profile.is_business_account}")
if profile.is_business_account == True:
  print(f"Business Category: {profile.business_category_name}")
print(f"Story up: {profile.has_viewable_story}")

print("\nBlocking..............")
print(f"Blocked by followers: {profile.blocked_by_viewer}")
print(f"Blocked Viewer: {profile.has_blocked_viewer}")

print("\nRequests............")
print(f"Viewer Request: {profile.requested_by_viewer}")
print(f"Reqest: {profile.has_requested_viewer}")

print("\nTop 10 Followers...........")
followers = profile.get_followers()
i = 1
for follower in followers:
  print(f"Follower: {follower.username}")
  i += 1
  if i == 10:
    break

print("\nTop 10 Following............")
followees = profile.get_followees()
i = 1
for followee in followees:
  print(f"Following: {followee.username}")
  i += 1
  if i == 10:
    break
