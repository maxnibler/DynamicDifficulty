from game_state import GameState

state = GameState()
print(state.getPlayerStats())

state.incrementPlayerStat('Strengh', 19)

print(state.getPlayerStats())
