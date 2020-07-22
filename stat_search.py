from game_state import GameState
from simulate import simulate_game

class simulate_node:
    key = None
    win = None
    health = None
    strength = None
    dexterity = None
    attackDamage = None
    parent = None
    def __init__(self, parent):
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
            self.attackDamage == a

    def execute(self, playerStats):
        enemyStats = {
            'Health' : health,
            'Strength' : strength,
            'Dexterity' : dexterity,
            'Attack Damage' : attackDamage
        }
        state = GameState(dict(playerStats), dict(enemyStats))

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
    total = pair[0] + pair[1]
    return total/2

def searchStats(playerStats, winrate):
    eStats = {}
    eStats['Health'] = 100
    eStats['Strength'] = 10
    eStats['Dexterity'] = 10
    eStats['Attack Damage'] = 10
    healthRange = (10, 200)
    strRange = (5, 40)
    dexRange = (5, 40)
    attackRange = (1, 40)
    root = node("Root", 0)
    root.printSelf()
    root = expand(root, 'Health', healthRange[0], healthRange[1], 1)
    for healthNode in root.getChildren():
        expand(healthNode, 'Strength', 1, 40, 1)
        for strNode in healthNode.getChildren():
            simNode = simulate_node(strNode)
            hDef = tupleRand(healthRange)
            sDef = tupleRand(strRange)
            dDef = tupleRand(dexRange)
            aDef = tupleRand(attackRange)
            simNode.setDefaults(hDef, sDef, dDef, aDef)
    
    return eStats
