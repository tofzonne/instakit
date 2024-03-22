import json
import os
from .init import banner

class Betamode:

    def __init__(self) -> None:
        pass
    
    def _showVictims(self) -> None:
        banner('a')
        folder = os.path.join(os.getcwd(), 'core', 'logs', '.Poeples')
        try:
            files = os.listdir(folder)
        except FileNotFoundError:
            return False
        # print(files)
        tempdict = {}
        for i in files:
            with open(os.path.join(folder,i)) as f:
                data = json.load(f)
            tempdict[i.replace('.json', '')] = data
        
        print(f'\n\nYou\'ve {len(tempdict)} users that you can analyze.\n')
        for count, i in enumerate(tempdict.keys(), 1):
            print(f'        {count}. {tempdict[i]["username"]}')
        print('\nSelect the id or username to proceed with that account.')
        self._input()