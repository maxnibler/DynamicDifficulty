import random
from game_state import GameState

class enemy_bot:
    def __init__(self, stats):
        self.stats = stats

    def change_stats(self, new_stats):
        self.stats = new_stats

    def behavior_tree_setup(self):
        root = Sequence(name = 'Main Enemy Node')

        dodging = Action('Dodge')
        l_attacking = Action('Light Attack')
        parrying = Action('Parry')
        h_attacking = Action('Heavy Attack')

        dex_execute = Sequence(name = "Dexterity Execute")
        dex_check = Check(dex_higher_than_str(self.stats))
        dex_branch = Selector(name = 'Dexterity Branch')
        health_check = Sequence(name = "Health Check")
        health_compare = Check(enemy_more_health(stats))
        dex_low_health = RandomSelector(name = "Dexterity Branch low Health")
        health_check.child_nodes = [health_compare, l_attacking]
        dex_low_health.child_nodes = [l_attacking, dodging]
        dex_branch.child_nodes = [health_check, dex_low_health]
        dex_execute.child_nodes = [dex_check, dex_branch]

        str_execute = Sequence(name = "Strength Execute")
        str_check = Check(str_higher_than_dex(self.stats))
        str_branch = Selector(name = "Strength Branch")
        health_check2 = Sequence("Health Check 2")
        str_low_health = RandomSelector(name = "Strength Branch low Health")
        health_check2.child_nodes = [health_compare, h_attacking]
        str_low_health.child_nodes = [h_attacking, parrying]
        str_branch.child_nodes = [health_check2, str_low_health]
        str_execute.child_nodes = [str_check, str_branch]

        neutral = Selector(name = "Dexterity and Strength equal")
        health_check3 = Sequence(name = "Health Check 3")
        rand_attack = RandomSelector(name = "Random Attack")
        rand_attack.child_nodes = [l_attacking, h_attacking]
        health_check3.child_nodes = [health_compare, rand_attack]
        all_actions = RandomSelector(name = "All Actions")
        all_actions.child_nodes = [l_attacking, h_attacking, parrying, dodging]
        neutral.child_nodes = [health_check3, all_actions]

        root.child_nodes = [dex_execute, str_execute, neutral]
        return root

# Nodes
class Node:
    def __init__(self):
        raise NotImplementedError

class Composite(Node):
    def __init__(self, child_nodes=[], name=None):
        self.child_nodes = child_nodes
        self.name = name

class Leaf(Node):
    def __init__(self, name=None):
        self.name = name

class Check(Node):
    def __init__(self, check_function):
        self.check_function = check_function

    def execute(self):
        return self.check_function()

# Composite Nodes
# Sequence Node code taken from P4
class Sequence(Composite):
    def execute(self):
        for child_node in self.child_nodes:
            continue_execution = child_node.execute()
            if not continue_execution:
                return False
        else:  # for loop completed without failure; return success
            return True

#Selector Node taken from P4
class Selector(Composite):
    def execute(self):
        for child_node in self.child_nodes:
            success = child_node.execute()
            if success:
                return True
        else:  # for loop completed without success; return failure
            return False

class RandomSequence(Composite):
    def execute(self):
        children = self.child_nodes
        while len(children) > 0:
            num = random.randint(0, len(children) - 1)
            child = children[num]
            child_value = child.execute()
            if child_value != False:
                to_continue = True
            if not to_continue:
                return False
            children.remove(child)
        return child_value

class RandomSelector(Composite):
    def execute(self):
        children = self.child_nodes
        while len(children) > 0:
            num = random.randint(0, len(children) - 1)
            child = children[num]
            child_value = child.execute()
            if child_value != False:
                return child_value
            children.remove(child)
        return False

# Checks
def dex_higher_than_str(stats):
    return (stats['Dexterity'] > stats['Strength'])

def str_higher_than_dex(stats):
    return (stats["Strength"] > stats["Dexterity"])

def enemy_more_health(stats):
    return (stats["Health"] > getPlayerStats()["Health"])

# Leaf Node
class Action(Leaf):
    def __init__(self, action_to_do):
        self.action_to_do = action_to_do

    def execute(self):
        return self.action_to_do
