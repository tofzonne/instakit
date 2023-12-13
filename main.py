import instaloader, sys
from getpass import getpass

def banner():
    print("""
'####:'##::: ##::'######::'########::::'###:::::::::::::'##:::'##:'####:'########:
. ##:: ###:: ##:'##... ##:... ##..::::'## ##:::::::::::: ##::'##::. ##::... ##..::
: ##:: ####: ##: ##:::..::::: ##:::::'##:. ##::::::::::: ##:'##:::: ##::::: ##::::
: ##:: ## ## ##:. ######::::: ##::::'##:::. ##:'#######: #####::::: ##::::: ##::::
: ##:: ##. ####::..... ##:::: ##:::: #########:........: ##. ##:::: ##::::: ##::::
: ##:: ##:. ###:'##::: ##:::: ##:::: ##.... ##:::::::::: ##:. ##::: ##::::: ##::::
'####: ##::. ##:. ######::::: ##:::: ##:::: ##:::::::::: ##::. ##:'####:::: ##::::
....::..::::..:::......::::::..:::::..:::::..:::::::::::..::::..::....:::::..:::::
            """)
        
def Print(message_type: str, message: str):
  """
  Prints a message with color and symbol based on its type.

  Args:
    message_type: The type of the message (warning, info, success, general).
    message: The message string to be printed.
  """
  colors = {
      "w": "\033[38;2;255;255;0m",
      "i": "\033[38;2;0;0;255m",
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

def info(username: str):


    profile = instaloader.Profile.from_username(L.context, username)


    Print('i', f"{profile.full_name}'s info...\n")
    print(f'Followers: {profile.followers}')



L = instaloader.Instaloader()

# banner()
Print('n', '1. Limited features')
Print('n', '2. Advanced Features Require Login\n\n')

opt = input('> ')

if opt == '2':
    Print('i', 'To login enter the credtial')
    username = input('\nUsername: ')
    pwd = getpass('> ')

    try:
        L.login(username,pwd)
        Print('s', 'Login Success')
    except:
        Print('w','Login Failed!')

target_user = input("\033[1;32mTarget username: \33[0m")
if len(target_user) <= 2:
    Print('d', "Username can't be empty")
    exit(1)

info(target_user)