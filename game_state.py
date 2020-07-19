class GameState:
    playerStats = {}
    enemyStats = {}
    
    def __init__(self):
        self.playerStats = {
            'Strength' : 0,
            'Dexterity' : 0,
            'Health' : 0,
            'Attack Damage' : 0
        }
        self.enemyStats = {
            'Strength' : 0,
            'Dexterity' : 0,
            'Health' : 0,
            'Attack Damage' : 0
        }
    
    def getPlayerStats(self):
        return self.playerStats

    def getEnemyStats(self):
        return self.enemyStats

    def setPlayerStats(self, s, d, h, a):
        self.playerStats['Strength'] = s
        self.playerStats['Dexterity'] = d
        self.playerStats['Health'] = h
        self.playerStats['Attack Damage'] = a

    def setEnemyStats(self, s, d, h, a):
        self.enemyStats['Strength'] = s
        self.enemyStats['Dexterity'] = d
        self.enemyStats['Health'] = h
        self.enemyStats['Attack Damage'] = a

    def incrementEnemyStat(self, key, amount):
        if key not in self.enemyStats:
            print(key+" is not a stat of enemy character")
            return
        else:
            self.enemyStats[key] += amount

    def incrementPlayerStat(self, key, amount):
        if key not in self.playerStats:
            print(key+" is not a stat of player character")
            return
        else:
            self.playerStats[key] += amount
