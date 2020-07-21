# REQURIRED LINES TO RUN AFTER IMPORTING FILE:
# Player_Bot = player_bot(stats)
# Player_Bot.behavior_tree_run()

import random

class player_bot:

    def __init__(self, stats):
        self.stats = stats

    def change_stats(self, new_stats):
        self.stats = new_stats

    def behavior_tree_setup(self):
        # Checks which stats are higher than others in order to weight those
        # more heavily in behavior tree
        highest_stat = None
        mid_stat = None
        lowest_stat = None
        for x in self.stats:
            if x != 'Health':
                if highest_stat == None or self.stats[x] > self.stats[highest_stat]:
                    lowest_stat = mid_stat
                    mid_stat = highest_stat
                    highest_stat = x
                elif mid_stat == None or (self.stats[x] <= self.stats[highest_stat] \
                and (lowest_stat == None or self.stats[x] >= self.stats[lowest_stat])):
                    lowest_stat = mid_stat
                    mid_stat = x
                elif lowest_stat == None or (self.stats[x] < self.stats[mid_stat]):
                    lowest_stat = x

        root = RandomSelector(name='Main Random Selector')

        # Tree selections based on stats in partially random system:
        # Highest stat has 3 branches
        # Middle stat has 2 branches
        # Lowest stat has 1 branch

        dex_branch = RandomSelector(name='Dex Branch')
        dodging = Action('Dodge')
        l_attacking = Action('Light Attack')
        dex_branch.child_nodes = [dodging, l_attacking]

        str_branch = RandomSelector(name='Strength Branch')
        parrying = Action('Parry')
        h_attacking = Action('Heavy Attack')
        str_branch.child_nodes = [parrying, parrying, h_attacking]

        ad_branch = RandomSelector(name='Attack Damage Branch')
        parrying = Action('Parry')
        h_attacking = Action('Heavy Attack')
        ad_branch.child_nodes = [parrying, h_attacking, h_attacking]

        if highest_stat == 'Dexterity':
            if mid_stat == 'Strength':
                root.child_nodes = [dex_branch, dex_branch, dex_branch, str_branch, str_branch, ad_branch]
            elif mid_stat == 'Attack Damage':
                root.child_nodes = [dex_branch, dex_branch, dex_branch, ad_branch, ad_branch, str_branch]
        elif highest_stat == 'Strength':
            if mid_stat == 'Dexterity':
                root.child_nodes = [str_branch, str_branch, str_branch, dex_branch, dex_branch, ad_branch]
            elif mid_stat == 'Attack Damage':
                root.child_nodes = [str_branch, str_branch, str_branch, ad_branch, ad_branch, dex_branch]
        else:
            if mid_stat == 'Dexterity':
                root.child_nodes = [ad_branch, ad_branch, ad_branch, dex_branch, dex_branch, str_branch]
            elif mid_stat == 'Strength':
                root.child_nodes = [ad_branch, ad_branch, ad_branch, str_branch, str_branch, dex_branch]

        return root


    def behavior_tree_run(self):
        behavior_tree = self.behavior_tree_setup()
        return behavior_tree.execute()


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


# Composite Nodes
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


# Leaf Node
class Action(Leaf):
    def __init__(self, action_to_do):
        self.action_to_do = action_to_do

    def execute(self):
        return self.action_to_do
