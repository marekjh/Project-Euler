import numpy as np
from collections import Counter

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

DEPTH = 1000

def main():
    T = []
    for si in range(N):
        for di in range(3):
            T.append(transition(si, di))
    T = np.array(T)
    v = np.zeros(3*N)
    v[0] = 1
    Tn = np.linalg.matrix_power(T, DEPTH)
    result = np.dot(v, T)
    print(condense(result))

def transition(si, di):
    t = []
    (m0, m1) = roll_moveset(si)
    full = (full_moveset(m0), full_moveset(m1))
    for sf in range(N):
        for df in range(3):
            diff = df - di
            if diff == -2:
                if sf == JAIL:
                    p = 1/D
                else:
                    p = 0
            elif diff not in (0, 1):
                p = 0
            else:
                p = full[diff][sf]
            t.append(p)
    return t

def full_moveset(roll_moves):
    full_moves = roll_moves
    for card_type in (CC, CH):
        for move in set(roll_moves).intersection(card_type):
            p = roll_moves[move]
            del roll_moves[move]
            new_moves = {k: p*v for k, v in card_moveset(move, card_type).items()}
            full_moves = Counter(roll_moves) + Counter(new_moves)
    return full_moves

def roll_moveset(si):
    moves = spaces(si+3, si+2*D)
    roll_probs = [x for x in range(2, D+1)] + [x for x in range(D-1, 1, -1)]
    roll_probs = np.array([x-1 if i%2 == 1 else x for i, x in enumerate(roll_probs)])/D**2
    m0 =  dict(zip(moves, roll_probs))  # No double rolled
    moves = spaces(si+2, si+2*D + 1, 2)
    roll_probs = np.array([1 for _ in range(len(moves))])/D**2
    m1 =  dict(zip(moves, roll_probs))  # Double rolled
    for m in (m0, m1):
        enforce_G2J(m)
    return (m0, m1)

def card_moveset(space, cc):
    if cc:
        return {space: 14*P_CARD, GO: P_CARD, JAIL: P_CARD}
    return {space: 6*P_CARD, GO: P_CARD, JAIL: P_CARD, C1: P_CARD, E3: P_CARD, H2: P_CARD, R[0]: P_CARD, 
            nearest(R, space): 2*P_CARD, nearest(U, space): P_CARD, space-3: P_CARD}

def condense(arr):
    result = []
    for i in range(N):
        slice = arr[3*i:3*(i+1)]
        result.append(sum(slice))
    return result


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