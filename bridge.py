"""
Different people cross the bridge at different speeds.
Which order should the people be send across the bridge
to cross it in the least time.
"""

def bsuccessors(state):
    here, there, t = state
    if 'light' in here:
        return dict(((here  - frozenset([a,b, 'light']),
                      there | frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here  | frozenset([a,b, 'light']),
                      there - frozenset([a, b, 'light']),
                      t + max(a, b)),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')  
        
def elapsed_time(path):
    return path[-1][2]

def bridge_problem(here):
    here = frozenset(here) | frozenset(['light'])
    explored = set() 
    frontier = [ [(here, frozenset(), 0)] ] 
    while frontier:
        path = frontier.pop(0)
        here1, there1, t1 = state1 = path[-1]
        if not here1 or here1 == set(['light']):
            return path
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
    return []



def path_states(path):
    return path[0::2]

def path_actions(path):
    return path[1::2]

def test():
    #frozensets are the immutable version of sets

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    assert [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(8)] == [0, 1, 1, 2, 6, 12, 19, 30]
    
    print('tests pass') 

test()