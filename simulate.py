from player_bot import player_bot
from enemy_bot import enemy_bot
from game_state import GameState
def simulate_game(state, game):
    Player_Bot = player_bot(state.getPlayerStats())

    Enemy_Bot = enemy_bot(state.getEnemyStats())

    # Makes copy of state for use in function
    curr_state = GameState(state.getPlayerStats(), state.getEnemyStats())

    while curr_state.getPlayerStats()['Health'] > 0 and curr_state.getEnemyStats()['Health'] > 0:
        Player_Bot.change_stats(curr_state.getPlayerStats())
        player_move = Player_Bot.behavior_tree_run()
        Enemy_Bot.change_stats(curr_state.getEnemyStats())
        enemy_move = Enemy_Bot.behavior_tree_run()

        curr_state = game.actionSet(player_move, enemy_move, curr_state)


    if curr_state.getPlayerStats()['Health'] <= 0 and curr_state.getEnemyStats()['Health'] <= 0:
        return 0
    elif curr_state.getEnemyStats()['Health'] <= 0:
        return 1
    else:
        return -1
