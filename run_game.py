from game_state import GameState
from game_actions import GameCalc
from simulate import simulate_game
from stat_search import searchStats

playerStats ={}
playerStats['Health'] = int(input("Enter Player Health: "))
playerStats['Strength'] = int(input("Enter Player Strength: "))
playerStats['Dexterity'] = int(input("Enter Player Dexterity: "))
playerStats['Attack Damage'] = int(input("Enter Player Attack Damage: "))

enemyStats = {}
# DO MCTS HERE for ENEMY STATS
enemyStats = searchStats(playerStats)

state = GameState(playerStats, enemyStats)
game = GameCalc()

player_wins = 0
enemy_wins = 0
ties = 0

for x in range(100):
    result = simulate_game(state, game)
    if result == 1:
        print("Player Bot Wins")
        player_wins +=1
    elif result == 0:
        print("Tie")
        ties += 1
    else:
        print("Enemy Bot Wins")
        enemy_wins += 1

print("Player Bot Win Rate:", player_wins, "%")
print("Enemy Bot Win Rate:", enemy_wins, "%")
print("Tie Game Rate:", ties, "%")
