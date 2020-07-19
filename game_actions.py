from game_state import GameState

#Helper Calculations
def HeavyAttack_Parry(attackerStats, defenderStats):
    aStrength = attackerStats['Strength']
    dStrength = defenderStats['Strength']
    if aStrength > dStrength:
        defenderStats['Health'] -= aStrength-dStrength
    else:
        defenderStats['Health'] -= 1
    return defenderStats

def HeavyAttack_Dodge(attackerStats, defenderStats):
    aDex = attackerStats['Dexterity']
    dDex = defenderStats['Dexterity']
    if dDex > aDex:
        attackerStats['Health'] -= dDex - aDex
    else:
        attackerStats['Health'] -= 1
    return attackerStats


class GameCalc:
    
    def __init__(self):
        self.actions = [
            'Dodge',
            'Parry',
            'Light Attack',
            'Heavy Attack'
        ]
        
    def actionSet(self, playerAction, enemyAction, state):
        if playerAction not in self.actions:
            print(playerAction+" is not a valid action")
            return
        elif enemyAction not in self.actions:
            print(enemyAction+" is not a valid action")
            return
        else:
            return self.calcTurn(playerAction, enemyAction, state)
            
    def calcTurn(self, playerAction, enemyAction, state):
        pStats = state.getPlayerStats()
        eStats = state.getEnemyStats()
        if playerAction == enemyAction:
            if playerAction == 'Light Attack':
                pAD = pStats['Attack Damage']
                eAD = eStats['Attack Damage']
                state.incrementEnemyStat('Health', -pAD)
                state.incrementPlayerStat('Health', -eAD)
            elif playerAction == 'Heavy Attack':
                pAD = pStats['Attack Damage']
                eAD = eStats['Attack Damage']
                pAD += pStats['Strength']
                eAD += pStats['Strength']
                state.incrementEnemyStat('Health', -pAD)
                state.incrementPlayerStat('Health', -eAD)
        else:
            if playerAction == 'Heavy Attack':
                if enemyAction == 'Parry':
                    eStats = HeavyAttack_Parry(pStats, eStats)
                    state.setEnemyStats(eStats)
                if enemyAction == 'Dodge':
                    pStats = HeavyAttack_Dodge(pStats, eStats)
                    state.setPlayerStats(pStats)
            elif playerAction == 'Parry':
                if enemyAction == 'Heavy Attack':
                    pStats = HeavyAttack_Parry(eStats, pStats)
                    state.setPlayerStats(pStats)
            elif playerAction == 'Dodge':
                if enemyAction == 'Heavy Attack':
                    eStats = HeavyAttack_Dodge(eStats, pStats)
                    state.setEnemyStats(eStats)
        
                
        return state
        
