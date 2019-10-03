"""
We have 2 flasks of capacity 9 litres and 4 liters. 
We need to calculate 6 litres using these two. 
We also have an unlimited source of water.
"""

def successors(x, y, X, Y):
    if (x <= X and y <= Y): #checking that the water levels are less than the glass can take
        return {
            ((0, y+x) if y+x<Y else (x - (Y-y), y + (Y-y))): 'X -> Y',
            ((y+x, 0) if y+x<X else (x + (X-x), y - (X-x))): 'X <- Y',
            (X, y): 'fill X', (x, Y): 'fill Y',
            (0, y): 'empty X', (x, 0): 'empty Y'
            }


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

print(pour_problem(9,4,2))