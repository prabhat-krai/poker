import re, itertools

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', 
        fill in digits that solve it."""
    for f in fill_in(formula):
        if(valid(f)):
            return f
    
def valid(f):
    try:
        return (not re.search(r'\b0[0-9]', f)) and eval(f) is True
    except ArithmeticError:
        return False

def fill_in(formula):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890',len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


test_cases = """A**2 + B**2 == C**2 and A > 1
TWO + TWO == FORE
COF + FEE*N == CO + FF + EE and N != 0""".splitlines()

def test():
    for test_case in test_cases:
        print(solve(test_case))

test()

#after checking the cProfile of the program we find that eval is slowing down the 
#program. So, we'll implement the functionality differently to speed up the 
#program. 