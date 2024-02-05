


# INSTAKIT

Instakit is a command-line tool written in Python that utilizes the Instaloader module to extract and display information about Instagram users. It offers a user-friendly interface and a range of features to help you gather data about Instagram accounts.

[![Run on Repl.it!](https://replit.com/badge/github/tofzonne/instakit)](https://replit.com/@tofzonne/instakit)<p>
    <a href="https://www.buymeacoffee.com/tofzonne">
        <img align="left"
            src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png"
            height="50"
            width="210"
            alt="Buy me a Coffe"
        />
    </a>
</p>


<br><br>

---


<!-- <p align="center">
  <a href="https://github.com/tofzonne/github-readme-stats/graphs/contributors">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/tofzonne/instakit" />
  </a>
  <a href="https://github.com/tofzonne/instakit/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/tofzonne/instakit?color=0088ff" />
  </a>
  <a href="https://github.com/tofzonne/instakit/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/tofzonne/instakit?color=0088ff" />
  </a>
</p> -->

# Features

- **Login Option:** Instakit provides the option to log in to your Instagram account to access additional information and perform certain actions.

- **Scan Usernames:** You can input a target username to scan and gather information about their Instagram profile.

- **Display Scanned Usernames:** Instakit maintains a log of all scanned usernames, allowing you to review and manage your scanned accounts.


- **Detailed Information:** For each username, Instakit displays a wealth of information, including:

  - User ID
  - Username
  - Full name **(if available)**
  - Pronouns **(if available)**
  - Recently joined status
  - Number of **Followers**
  - Number of **Followings**
  - Bio **(if available)**
  - External URL **(if available)**
  - Follow/following status ***(if logged in)***
  - Request/requested status ***(if logged in)***
  - Total number of posts
  - Private account status
  - Verified account status
  - Professional account status
  - Professional account category **(if available)**
  - Business account status
  - Business account category **(if applicable)**
  - Business email **(if available)**
  - Business phone **(if available)**
  - Supervision status
  - Supervisor status ***(if logged in)***
  - Supervisee status ***(if logged in)***
  - Guardian ID **(if applicable)**
  - Blocked/restricted status ***(if logged in)***
  - Guides availability
  - Mutual followers ***(if logged in)***

- **Save Information:** You can choose to save the displayed information about a scanned username to a text file for future reference.

- **Profile Picture Download:** Instakit allows you to download the profile picture of the scanned username.

- **Recent Posts Download:** You can opt to download upto `50` most recent posts from the scanned username's profile.
*Or more if you want to.*

- **Clear Logs:** You can clear the log of scanned usernames at any time.

# Tested on
**Linux.** & **Windows**
# Requirements
- Python
- Instaloader

# Installation

To install `Instakit`, follow these steps:

1. Ensure you have Python 3 or higher installed on your system.
2. Open a terminal or command prompt.
3. Clone the Instakit repository using the following command:

```console
git clone https://github.com/tofzonne/instakit.git
```

4. Navigate to the Instakit directory:

```console
cd Instakit
```

5. Install the required Python modules using the following command:

```console
pip install -r requirements.txt
```

# Usage

To use **Instakit**, follow these steps:

1. Open a terminal window or cmd and navigate to the Instakit directory.
2. Run the following command to start the tool:

```console
python main.py
```

3. Follow the on-screen instructions to log in to your Instagram account **(optional)** and scan usernames.
4. Select the desired options from the menu to **view**, **save**, or **download** information about scanned usernames.

# Tips
*For those already using Instakit.*
- Uninstall instaloader and reinstall it by running `pip install -r requirements.txt`, or you'll encounter login errors. ***Important**

- If you accidentally selected `a` option from the main screen and **don't want to scan**, you can enter `.b` in place of the `username: ` field to return to the previous menu.

- If you've logged in and tried to run main.py again, the tool will prompt you to select your previous session. Alternatively, if you want to continue without logging in, simply **enter negative values, e.g** `-1`.

# Experiments

If you want to try **beta** version of `instakit` then please checkout to `beta` branch before running the `main.py` file and check for updates regularly. like this


**Update your local branch first.**
```
git pull
```
```
git checkout beta
```

# Contributing

**Contributions to Instakit are welcome!** If you have any suggestions, bug fixes, or new features you'd like to add, please feel free to create a pull request.

# License

Instakit is licensed under the **MIT License**.

# Thanks
You're welcome 🤗.
