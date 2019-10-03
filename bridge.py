"""
Different people cross the bridge at different speeds.
Which order should the people be send across the bridge
to cross it in the least time.
"""

def successors(state):
    #taka a state and return a dictionary of state action pairs.
    here, there, t = state
    


















def test():
    #frozensets are the immutable version of sets

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'