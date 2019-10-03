"""
We have 2 flasks of capacity 9 litres and 4 liters. 
We need to calculate 6 litres using these two. 
We also have an unlimited source of water.
"""

def pour_problem(X, Y, goal, start = (0,0)):
    if goal in start:
        return [start] #converting into list while returning

    explored = set()
    frontier = [[ start ]]
    while frontier:
        path = frontier.pop(0) #first path
        (x, y) = path[-1]     #last state
        for (state, action) in successors(x, y, X,Y).items():
            if state not in explored:
                explored.add(state)
                path_new = path + [action, state]
                if goal in state:
                    return path_new
                else:
                    frontier.append(path_new)

    return "Failed to find a way to reach the goal"

