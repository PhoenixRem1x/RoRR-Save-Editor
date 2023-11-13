import json
characters = ['acrid','arti','bandit','loader','hand','mercenary','pilot','sniper','enforcer','drifter','engineer','chef','miner',]
def unlockview(character):
    unlock = f'challenge_unlock_{character}_completed'
    view = f'survivor_{character}_viewed'
    return unlock,view

path = 'save.json'
with open(path, 'r') as infile:
    jsn = json.load(infile)
flags = jsn["flags"]
#print(flags)

def checkCharacters():
    for value in characters:
        unlock,view = unlockview(value)
        if unlock in flags:
            print(f'{value.upper()} Is Unlocked [✅]')
        else:
            print(f'{value.upper()} Is Locked [❌]')

def main():
    pass