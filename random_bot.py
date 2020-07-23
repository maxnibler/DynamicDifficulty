import random

random.seed(0)

def randBot():
    actions = [
        'Dodge',
        'Parry',
        'Light Attack',
        'Heavy Attack'
    ]
    ind = random.randrange(len(actions))
    return actions[ind]

