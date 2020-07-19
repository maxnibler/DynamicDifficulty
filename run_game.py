from game_state import GameState
from game_actions import GameCalc

state = GameState()
game = GameCalc()
state = game.actionSet('Heavy Attack', 'Light Attack', state)
print(state.getPlayerStats())
print(state.getEnemyStats())
