import string, re

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', 
        fill in digits that solve it."""

    
def valid(f):
    try:
        return not re.search(r'\b0[0-9', f) and eval(f) is True
    except ArithmeticError:
        return False