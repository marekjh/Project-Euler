import sympy as sp

def solve_system():
    vars = (x1, x2, x3, x4, x5, x6, x7, x8, x9) = sp.symbols("x1 x2 x3 x4 x5 x6 x7 x8 x9", integer=True)
    exp1 = 10 + x1 + x2
    exp2 = x6 + x2 + x3
    exp3 = x7 + x3 + x4
    exp4 = x8 + x4 + x5
    exp5 = x9 + x5 + x1
    eqns = sp.Eq(exp1, exp2), sp.Eq(exp2, exp3), sp.Eq(exp3, exp4), sp.Eq(exp4, exp5)
    print(sp.linsolve(eqns, vars))