import numpy as np

N = 40
D = 6

GO = 0
JAIL = 10
G2J = 30
C1 = 11
E3 = 24
H2 = 39
R = [5, 15, 25, 35]
U = [12, 28]
CC = {2, 17, 33}     
CH = {7, 22, 36} 
P_CARD = 1/16

def main():
    pass

def transition(si, di):
    for sf in range(N):
        for df in range(3):
            pass
        
def moveset(si):
    M = []
    moves = spaces(si+3, si+2*D)
    roll_probs = [x for x in range(2, D+1)] + [x for x in range(D-1, 1, -1)]
    roll_probs = np.array([x-1 if i%2 == 1 else x for i, x in enumerate(roll_probs)])/D**2
    M[0] =  dict(zip(moves, roll_probs))  # No double rolled
    moves = spaces(si+2, si+2*D + 1, 2)
    roll_probs = np.array([1 for _ in range(len(moves))])/D**2
    M[1] =  dict(zip(moves, roll_probs))  # Double Rolled
    M[2]  =  {JAIL: 1/D}  # Third double rolled
    for m in M:
        enforce_G2J(m)
    return M

def card_moveset(space, cc):
    if cc:
        return {space: 14*P_CARD, GO: P_CARD, JAIL: P_CARD}
    return {space: 6*P_CARD, GO: P_CARD, JAIL: P_CARD, C1: P_CARD, E3: P_CARD, H2: P_CARD, R[0]: P_CARD, 
            nearest(R, space): 2*P_CARD, nearest(U, space): P_CARD, space-3: P_CARD}

def spaces(start, end, step=1):
    return np.array(range(start, end, step)) % N

def nearest(arr, e):
    for a in arr:
        if a > e:
            return e
    return R[0]

def enforce_G2J(moves):
    if G2J in moves:
        if JAIL in moves:
            moves[JAIL] += moves[G2J]
        else:
            moves[JAIL] = moves[G2J]
        del moves[G2J]

def state(space, doubles):
    return 3*space + doubles

if __name__ == "__main__":
    main()