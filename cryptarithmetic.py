import re, itertools, time

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
COF + FEE == CA + QWK + IOP""".splitlines()

def test():
	for test_case in test_cases:
		print(solve(test_case))

def fast_test():
    for test_case in test_cases:
        print(faster_solve(test_case))


#after checking the cProfile of the program we find that eval is slowing down the 
#program. So, we'll implement the functionality differently to speed up the 
#program. 

def compile_word(word):
    if word.isupper():
        terms = [('%s%s%s' % (10**i,'*',d))
                for (i,d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) +')'
    else:
        return word




def faster_solve(formula):
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass

def compile_formula(formula, verbose = False):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (params, body)
    if verbose: 
        print (f)
    return eval(f), letters

test()
fast_test()