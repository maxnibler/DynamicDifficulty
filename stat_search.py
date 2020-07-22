from game_state import GameState

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
        
def searchStats(playerStats, winrate):
    eStats = {}
    eStats['Health'] = 100
    eStats['Strength'] = 10
    eStats['Dexterity'] = 10
    eStats['Attack Damage'] = 10
    root = node("Root", 0)
    root.printSelf()
    root = expand(root, 'Health', 1, 100, 1)
    for c in root.getChildren():
        expand(c, 'Strength', 1, 40, 1)
    return eStats
