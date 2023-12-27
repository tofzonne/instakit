# INSTAKIT

Instakit is a command-line tool written in Python that utilizes the Instaloader module to extract and display information about Instagram users. It offers a user-friendly interface and a range of features to help you gather data about Instagram accounts.

[![Run on Repl.it](https://replit.com/badge/github/tofzonne/instakit)](https://replit.com/@tofzonne/instakit)
# Features

- **Login Option:** Instakit provides the option to log in to your Instagram account to access additional information and perform certain actions.

- **Scan Usernames:** You can input a target username to scan and gather information about their Instagram profile.

- **Display Scanned Usernames:** Instakit maintains a log of all scanned usernames, allowing you to review and manage your scanned accounts.

- **Detailed Information:** For each scanned username, Instakit displays a wealth of information, including:
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

- **Recent Posts Download:** You can opt to download the five most recent posts from the scanned username's profile.

- **Clear Logs:** You can clear the log of scanned usernames at any time.

# Tested on
**Windows** & **Termux.**
# Requirements
- Python
- Instaloader

# Installation

To install INSTAKIT, follow these steps:

1. Ensure you have Python 3 or higher installed on your system.
2. Open a terminal window or command prompt.
3. Clone the INSTAKIT repository using the following command:

```
git clone https://github.com/tofzonne/instakit.git
```

4. Navigate to the Instakit directory:

```
cd Instakit
```

5. Install the required Python modules using the following command:

```
pip install -r requirements.txt
```

# Usage

To use Instakit, follow these steps:

1. Open a terminal window or command prompt and navigate to the Instakit directory.
2. Run the following command to start the tool:

```
python main.py
```

3. Follow the on-screen instructions to log in to your Instagram account **(optional)** and scan usernames.
4. Select the desired options from the menu to **view**, **save**, or **download** information about scanned usernames.

# Contributing

Contributions to Instakit are welcome! If you have any suggestions, bug fixes, or new features you'd like to add, please feel free to create a pull request.

# License

Instakit is licensed under the MIT License. <br>

# Experiments

If you want to try **experimental** version of `instakit` then please checkout to `develop` branch before running the `main.py` file and check for updates regularly. like this<br>
Switching branch
```
git checkout develop
```
Getting updates
```
git pull
```
# Thanks
You're welcome 🤗.
