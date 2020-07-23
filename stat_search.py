from game_state import GameState
from simulate import simulate_game
import random

class simulate_node:
    key = None
    win = None
    health = None
    strength = None
    dexterity = None
    attackDamage = None
    parent = None
    def __init__(self, parent):
        self.win = 0
        self.key = "Simulate"
        self.parent = parent
        while parent.key != "Root":
            if parent.key == 'Attack Damage':
                self.attackDamage = parent.value
            if parent.key == 'Health':
                self.health = parent.value
            if parent.key == 'Dexterity':
                self.dexterity = parent.value
            if parent.key == 'Strength':
                self.strength = parent.value
            parent = parent.parent
            
    def printSelf(self):
        print("Win?:",self.win)
        print("Health:",self.health,"Strength:",self.strength,\
              "Dexterity:",self.dexterity,"Attack Damage:",
              self.attackDamage)

    def setDefaults(self, h, s, d, a):
        if self.health == None:
            self.health = h
        if self.strength == None:
            self.strength = s
        if self.dexterity == None:
            self.dexterity = d
        if self.attackDamage == None:
            self.attackDamage = a

    def execute(self, playerStats):
        enemyStats = {
            'Health' : self.health,
            'Strength' : self.strength,
            'Dexterity' : self.dexterity,
            'Attack Damage' : self.attackDamage
        }
        state = GameState(dict(playerStats), dict(enemyStats))
        total = 0
        for i in range(10):
            result = simulate_game(state)
            if result > 0:
                total += 1
        return total/10

class node:
    key = ""
    value = 0
    parent = None
    children = None
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.children = []

    def addChild(self, n):
        self.children.append(n)

    def setParent(self, n):
        self.parent = n

    def getStatSet(self):
        stats = {}
        temp = self
        while temp.key != "Root":
            stats[temp.key] = value
            temp = temp.parent
        return stats

    def getChildren(self):
        return list(self.children)
    
    def printSelf(self):
        print("Key:", self.key, "Value:", self.value)
        
def expand(parent, key, low, high, increment):
    i = low
    while i < high:
        newChild = node(key, i)
        #newChild.printSelf()
        parent.addChild(newChild)
        newChild.setParent(parent)
        i += increment
    return parent

def tupleRand(pair):
    if pair[0] == pair[1]:
        return pair[0]
    rand = random.randrange(pair[0], pair[1])
    return rand

def findStat(key, ranges, playerStats, winrate):
    statRange = ranges[key]
    root = node("Root", 0)
    root = expand(root, key, statRange[0], statRange[1], 1)
    fitNodes = []
    for currNode in root.getChildren():
        simNode = simulate_node(currNode)
        hDef = tupleRand(ranges['Health'])
        sDef = tupleRand(ranges['Strength'])
        dDef = tupleRand(ranges['Dexterity'])
        aDef = tupleRand(ranges['Attack Damage'])
        simNode.setDefaults(hDef, sDef, dDef, aDef)
        if winrate == simNode.execute(playerStats):
            fitNodes.append(currNode)
    ind = 0
    if len(fitNodes) < 1:
        print("Error: no value found for", key)
        theList = root.getChildren()
        i = round(len(theList)/2)
        return theList[i].value
    if len(fitNodes) > 1:
        ind = len(fitNodes) / 2
        ind = round(ind)
    return fitNodes[ind].value


def searchStats(playerStats, winrate):
    ranges = {
        'Health': (10, 200),
        'Strength': (5, 40),
        'Dexterity': (5, 40),
        'Attack Damage': (1, 40)
    }
    winrate = winrate/100
    winrate = round(winrate, 1)
    health = findStat('Health', ranges, playerStats, winrate)
    ranges['Health'] = (health, health)
    str = findStat('Strength', ranges, playerStats, winrate)
    ranges['Strength'] = (str, str)
    dex = findStat('Dexterity', ranges, playerStats, winrate)
    ranges['Dexterity'] = (dex, dex)
    ad = findStat('Attack Damage', ranges, playerStats, winrate)
    eStats = {}
    eStats['Health'] = health
    eStats['Strength'] = str
    eStats['Dexterity'] = dex
    eStats['Attack Damage'] = ad
    print(eStats)
    return eStats
