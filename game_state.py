class GameState:

    playerStats = {}
    enemyStats = {}

    def __init__(self, playerStats, enemyStats):
        self.playerStats = playerStats
        self.enemyStats = enemyStats

    def getPlayerStats(self):
        return self.playerStats

    def getEnemyStats(self):
        return self.enemyStats

    def setPlayerStats(self, statDict):
        self.playerStats = statDict

    def setEnemyStats(self, statDict):
        self.enemyStats = statDict

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
