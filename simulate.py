from player_bot import player_bot
from enemy_bot import enemy_bot
from random_bot import randBot
from game_actions import GameCalc
from game_state import GameState
def simulate_game(state):
    game = GameCalc()
    Player_Bot = player_bot(state.getPlayerStats())

    Enemy_Bot = enemy_bot(state.getEnemyStats())

    # Makes copy of state for use in function
    curr_state = state.copy()

    while curr_state.getPlayerStats()['Health'] > 0 and curr_state.getEnemyStats()['Health'] > 0:
        Player_Bot.change_stats(curr_state.getPlayerStats())
        player_move = Player_Bot.behavior_tree_run()
        #Enemy_Bot.change_stats(curr_state.getEnemyStats())
        enemy_move = Enemy_Bot.behavior_tree_run()
        #enemy_move = Enemy_Bot.behavior_tree_run()
        #print("Player move: "+player_move)
        #print("Enemy move: "+enemy_move)
        curr_state = game.actionSet(player_move, enemy_move, curr_state)


    if curr_state.getPlayerStats()['Health'] <= 0 and curr_state.getEnemyStats()['Health'] <= 0:
        return 0
    elif curr_state.getEnemyStats()['Health'] <= 0:
        return 1
    else:
        return -1
