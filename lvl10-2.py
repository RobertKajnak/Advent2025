import numpy as np
import re
import random

S = 0
rows = []
switchboard = []
targets = []
with open("lvl10-1.txt", "r") as f:
    for line in f.readlines():
        # raw = line.split()
        targets.append(tuple(int(t) for t in re.findall(r"\{(.+)\}", line)[0].split(",")))
        switchboard.append(
            [
                tuple(int(ss) for ss in s.split(","))
                for s in re.findall(r"\((.*?)\)", line)
            ]
        )

def flip_swithces(current, action, direction = 1):
    for switch_index in action:
        current[switch_index] += direction


def bruteforce(current,
                actions, 
                max_depth :int= 5, 
                current_depth :int= 0,):
    
    
    for action in actions:
        flip_swithces(current, action, -1)
        if any((x<0 for x in current)):
            flip_swithces(current, action, 1)
            continue
        actions_taken = []
        if current_depth<max_depth:
            # remaining_actions = list(actions)
            # remaining_actions.remove(action)
            actions_taken = bruteforce(current, actions, max_depth=max_depth, current_depth=current_depth+1)

        if not any(current):
            if actions_taken is None:
                print(current, actions_taken, actions)
            return actions_taken + [action]
        else:
            flip_swithces(current, action, 1)
    return None

S = 0
for line_index in range(len(targets)):
    actions = switchboard[line_index]
    target = targets[line_index]
    # current = [False] * len(target)
    # Starting from an all off position and reaching the target
    # is identical to starting with the target and flipping all the switches
    current = list(target)
    print(current)
    # take_action(current, actions, -1)
    # take_action(current, actions, -2)
    random.shuffle(actions)
    # print(current)
    for i in range(max(current)-1,sum(current)):
        actions_taken = bruteforce(current, actions, max_depth=i)
        if actions_taken:
            break
    # print(current)
    print(actions_taken)
    S += len(actions_taken)

    print(f"---{line_index+1}/{len(targets)}")



print(S)