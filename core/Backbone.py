from pathlib import Path
import platform
import instaloader

from datetime import datetime
import os

import requests


class Loader:

    def __init__(self) -> None:
        self.L = instaloader.Instaloader()
        self.profile = None
        self.is_logged_in = self.L.context.is_logged_in
        self.directory_path = None
        
    def _banner(self, mode: str = '') -> None:
        """
        Clears the Screen and prints the banner
        """
        asd = {'a': '\033[38;2;255;0;0m'}
        color = asd.get(mode, '\033[92m')
        
        os.system('cls') if platform.system() == 'Windows' else os.system('clear')

        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        flname = os.path.join(os.getcwd(), 'core', 'logs', 'info.log')

        logs_path = Path(flname)
        logs = logs_path.read_text().splitlines() if logs_path.exists() else []
        
        today = now.strftime("%d-%m-%y")
        tcount = sum(1 for line in logs if datetime.strptime(line.split(',')[1].strip(), '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%y') == today)
        srno = "" if tcount == 0 else f"Scanned today: {tcount}/{len(logs)} users"

        bann = f'\033[0mLogged in as:\033[92m {self.L.test_login()}\033[0m' if self.is_logged_in else ""
        # bann = ""

        print(
            f"""
Time: {time}                    {srno}{color} 
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗  ██╗██╗████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║ ██╔╝██║╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║█████╔╝ ██║   ██║   {bann}
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔═██╗ ██║   ██║
██║██║ ╚████║███████║   ██║   ██║  ██║██║  ██╗██║   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝\033[0m"""
)

    def _input(self, prompt: str = ''):
        """
        A modified input function for Beta mode & OOP only
        """
        if prompt: print(prompt)
        print('\n\nInstakit')
        user_input = input('    |==> ')
        return user_input

    def print(self, msg_type: str, msg: str) -> None:
        """
        prints a message to the console with color and symbol formatting based on message type.

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

        if msg.startswith('\n'):
            print(f'\n{color}{symbol}{msg[1:]}\033[0m')
        else:
            print(f"{color}{symbol}{msg}\033[0m")

    def _log(self):
        """
        Logs a user's activity to a file named `info.log` in the `core/logs` directory.

        Args:
            None
        """
        path = os.path.join(self._getRoot(),
                            'core',
                            'logs')
        os.makedirs(path, exist_ok=True)
        flname = os.path.join(path, 'info.log')
        with open(flname, 'a') as f:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{self.profile.username}, {time}, {self.profile.userid}\n")

        dp_url = self.profile.profile_pic_url
        dp_path = os.path.join(
            self.directory_path, 
            'Dp-{}.jpg'.format(self.profile.username)
        )
        
        self._getFile(url=dp_url, destination=dp_path)

    def _profile(self, username: str):
        """
        Fetches an Instagram profile object for the given username.

        This function attempts to retrieve the profile object for a specified username
        using the `instaloader` library. It handles various exceptions that might
        occur during the process:

        * `ConnectionException`: In case of network issues
            during profile retrieval.
        * `ProfileNotExistsException`: If the provided
            username doesn't correspond to an existing profile.
        * `LoginRequiredException`: If the user needs to be
            logged in to access the profile.
        * `QueryReturnedBadRequestException`: For any other
            unexpected errors returned by the Instagram API.

        If any exception occurs, the function displays informative messages
        indicating the error and prompts the user to retry or take necessary actions
        (e.g., login). On successful retrieval, the function stores the profile object
        in the `self.profile` attribute and calls the `self._log()` method (presumably
        for logging purposes).

        Args:
            username (str): The username of the Instagram profile to retrieve.

        Raises:
            SystemExit: If a `LoginRequiredException` occurs and the user chooses
                        to exit.
        """
        while True:
            try:
                profile = instaloader.Profile.from_username(self.L.context, username)
                break

            except instaloader.exceptions.ConnectionException as e:
                self._banner()
                self.print('d', f'\n{e}')
                self.print('w', 'Please Try again')

            except instaloader.exceptions.ProfileNotExistsException as e:
                self._banner()
                self.print('d', f'\nUser "{username}" does not Exists: {e}')
                self.print('w', 'Check Spelling and Try again')
                username = input('Enter the username: ')

            except instaloader.exceptions.LoginRequiredException as r:
                self._banner()
                self.print('w', f'\n{r}')
                self.print('d', 'Try again or login first')
                exit('Exiting ...')

            except instaloader.exceptions.QueryReturnedBadRequestException as b:
                self._banner('a')
                self.print('w', f'\n{b}')
                self.print('d', f'Bad Request')
                exit('Exiting ...')

        self.profile = profile
        self._createDirectory()

    def _getFile(self, url: str, destination: str) -> None:
        
        response = requests.get(url)
        if response.status_code == 200:
            with open(destination, 'wb') as file:
                file.write(response.content)
        else:
            self.print(
                'w',
                'Failed to download file. Status code: {}'.format(response.status_code))
            
    def _getRoot(self) -> str:
        """
        Gets the absolute path of the root directory relative to the current script's location.

        This function assumes that the root directory is two levels above the script's
        directory. If the root directory is located differently, adjust the relative path
        argument accordingly.

        Returns:
            str: The absolute path of the root directory.
        """
        abspath = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(abspath, '../')

        return path

    def _createDirectory(self):
        directoryName = self.profile.username + '_' + str(self.profile.userid)
        abspath = self._getRoot()
        path = os.path.join(abspath, 'temp', directoryName)
        os.makedirs(path, exist_ok=True)
        self.directory_path = path
        self._log()
        return path

    def download(self):

        def _createPath(post, sideCarNode = False, index = 0):
            prepath = self.directory_path

            uploaddate = str(post.date)
            filename = uploaddate.replace(':', '-')

            extension = 'mp4' if post.is_video else 'jpg'

            directory = os.path.join(prepath, 'Posts')
            os.makedirs(directory, exist_ok=True)

            if sideCarNode:
                path = os.path.join(
                    directory,
                    f'{filename}_{index}.'
                )
            else:
                path = os.path.join(
                    directory,
                    f'{filename}.{extension}'
                    )
            return path
            
        def _already_downloaded(path) -> bool:
            if not os.path.isfile(path):
                return False
            else:
                self.print('w', 'Already downloaded, skiping...')
                return True
            
        def _downloadPost(post):
            if post.typename == 'GraphSidecar': # line 729

                for i, sidecar_node in enumerate(post.get_sidecar_nodes(start = 1), 1):
                    sidecar_filename = _createPath(post=post, sideCarNode=True, index=i)
                    if sidecar_node.is_video:
                        sidecar_filename += 'mp4'
                    else:
                        sidecar_filename += 'jpg'
                    if not _already_downloaded(path=sidecar_filename):
                        if sidecar_node.is_video:
                            url = sidecar_node.video_url
                        else:
                            url = sidecar_node.display_url
                        self._getFile(url=url, destination=sidecar_filename)
            else:
                filename = _createPath(post=post)
                if not _already_downloaded(filename):
                    if post.is_video:
                        url = post.video_url
                    else:
                        url = post.url
                    self._getFile(url=url, destination=filename)
            self.print('s', 'Post downloaded')

        posts_count = self.profile.mediacount
        if posts_count <= 0:
            self.print('w', f'\n0 post found from {self.profile.username}\'s profile.')
            self.print('i', 'Nothing to download.')
            self._input()
        elif self.profile.is_private and not self.is_logged_in:
            self.print('w', f"\n{self.profile.username} has {posts_count} posts, but it's private.")
            self.print('d', "Can't download posts of private accounts.")
            self.print('i', f"Unless you log in and follow {self.profile.username}\n")
        else:
            self.print('i', 'Enter # of posts to Download.')
            post_to_download = self._input(f'Max # : {min(posts_count, 100)}')
            
            if post_to_download != '0':
                download_post = True

        if download_post:
            self._banner('a')
            posts = self.profile.get_posts()
            for i, post in enumerate(posts):
                if i == post_to_download: break
                _downloadPost(post=post)

    def showUserData(self):

        ...

    


sd = Loader()
sd._banner('a')
usrname = sd._input('Enter a username to test')
sd._profile(username=usrname)
print('\n\nfollowers', sd.profile.followers) # type: ignore

sd.download()