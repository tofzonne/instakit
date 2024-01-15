from datetime import datetime

class UserProfile:
    """
    Takes `_metadata` from instaloader Profile and returns a `UserProfile` object.
    """
    def __init__(self, data):
        self.data = data
    @property
    def username(self) -> str:
        return self.data('username')
    @property
    def full_name(self) -> str:
        return self.data('full_name')
    @property
    def biography(self) -> str:
        return self.data('biography')
    @property
    def external_url(self) -> str:
        return self.data('external_url')
    @property
    def blocked_by_viewer(self) -> bool:
        return self.data('blocked_by_viewer')
    @property
    def restricted_by_viewer(self) -> bool:
        return self.data('restricted_by_viewer')
    @property
    def followers(self) -> int:
        return self.data('edge_followed_by', 'count')
    @property
    def followees(self) -> int:
        return self.data('edge_follow', 'count')
    @property
    def has_guides(self) -> bool:
        return self.data('has_guides')
    @property
    def id(self) -> int:
        return int(self.data('id'))
    @property
    def is_business_account(self) -> bool:
        return self.data('is_business_account')
    @property
    def is_professional_account(self) -> bool:
        return self.data('is_professional_account')
    @property
    def category_name(self) -> str:
        return self.data('category_name')
    @property
    def is_supervision_enabled(self) -> bool:
        return self.data('is_supervision_enabled')
    @property
    def is_guardian_of_viewer(self) -> bool:
        return self.data('is_guardian_of_viewer')
    @property
    def is_supervised_by_viewer(self) -> bool:
        return self.data('is_supervised_by_viewer')
    @property
    def is_supervised_user(self) -> bool:
        return self.data('is_supervised_user')
    @property
    def is_joined_recently(self) -> bool:
        return self.data('is_joined_recently')
    @property
    def guardian_id(self) -> int:
        return self.data('guardian_id')
    @property
    def business_email(self) -> str:
        return self.data('business_email')
    @property
    def business_phone(self) -> str:
        return self.data('business_phone_number')
    @property
    def business_category_name(self) -> str:
        return self.data('business_category_name')
    @property
    def is_private(self) -> bool:
        return self.data('is_private')
    @property
    def is_verified(self) -> bool:
        return self.data('is_verified')
    @property
    def mutual_followed_by(self) -> dict:
        return self.data('edge_mutual_followed_by')
    @property
    def pronouns(self) -> list:
        return self.data('pronouns')
    
    
def followers(profile: object) -> dict:
    """
    Takes a profile object and returns a dictionary of followers.
    """
    follower = {}
    fobj = profile.get_followers()
    for sr, i in enumerate(fobj, 1):
        follower[sr] = {'username': i.username, 'name': i.full_name, 'id': i.id}
    return follower

def following(profile: object) -> dict:
    """
    Takes a profile object and returns a dictionary of followees.
    """
    followee = {}
    fobj = profile.get_followees()
    for sr, i in enumerate(fobj, 1):
        followee[sr] = {'username': i.username, 'name': i.full_name, 'id': i.id}
    return followee

def unique_users(data):
    unique = {}
    print('\n╭─────────────────────────────────────────────╮')
    print('│{:^45}│'.format('Scanned users (unique)'))
    print('├─────┬─────────────────────────┬─────────────┤')
    print('│{: ^5}│{: ^25}│ {: ^11} │'.format('Srno', 'Username', 'Scanned at'))
    print('├─────┼─────────────────────────┼─────────────┤')
    for line in reversed(data):
        user = line.split(',')[0].strip()
        raw = line.split(',')[1].strip()
        Raw = datetime.strptime(raw, '%Y-%m-%d %H:%M:%S')
        time = Raw.strftime('%H:%M %d/%m')
        if user not in unique:
            unique[user] = time
    count = 0
    for user, time in unique.items():
        count += 1
        print(f'│{count: ^5}│{user: ^25}│ {time: ^8} │')
    print('├─────┴──────────────────┬──────┴─────────────┤')
    print('│   c: Clear Log{: ^20}q: Quit   │'.format('│'))
    print('╰────────────────────────┴────────────────────╯\n')

def all_users(data):
    print('\n╭─────────────────────────────────────────────╮')
    print('│{:^45}│'.format('Scanned users (all)'))
    print('├─────┬─────────────────────────┬─────────────┤')
    print('│{: ^5}│{: ^25}│ {: ^11} │'.format('Srno', 'Username', 'Scanned at'))
    print('├─────┼─────────────────────────┼─────────────┤')
    for s, i in enumerate(reversed(data),1):
        username = i.split(',')[0].strip()
        rawT = i.split(',')[1].strip()
        Time = datetime.strptime(rawT, '%Y-%m-%d %H:%M:%S')
        print(f'│{s: ^5}│{username: ^25}│ {Time.strftime("%H:%M %m/%d"): ^8} │')
    print('├─────┴──────────────────┬──────┴─────────────┤')
    print('│   c: Clear Log{: ^20}q: Quit   │'.format('│'))
    print('╰────────────────────────┴────────────────────╯\n')
