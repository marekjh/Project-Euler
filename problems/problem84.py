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
R1 = 5
R = [5, 15, 25, 35]
U = [12, 28]
CC = {2, 17, 33}     
CH = {7, 22, 36} 
P_CARD = 1/16

DEPTH = 10000

def main():
    T = []
    for si in range(N):
        for di in range(3):
            T.append(transition(si, di))
    T = np.array(T)
    v = np.zeros(3*N)
    v[0] = 1
    Tn = np.linalg.matrix_power(T, DEPTH)
    result = condense(np.dot(v, Tn))
    print(sorted([x for x in enumerate(result)], key=lambda k: k[1], reverse=True))

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
                moves = full[diff]
                if sf in moves:
                    p = moves[sf]
                else:
                    p = 0
            t.append(p)
    if sum(t) < 0.999:
        print(sum(t), si, di)
    return t

def full_moveset(roll_moves):
    for card_type in (CC, CH):
        for move in set(roll_moves).intersection(card_type):
            p = roll_moves[move]
            del roll_moves[move]
            card_moves  = card_moveset(move, card_type)
            new_moves = {k: p*v for k, v in card_moves.items()}
            roll_moves = Counter(roll_moves) + Counter(new_moves)
    return roll_moves

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

def card_moveset(space, type):
    if type == CC:
        return {space: 14*P_CARD, GO: P_CARD, JAIL: P_CARD}
    m = {space: 6*P_CARD, GO: P_CARD, JAIL: P_CARD, C1: P_CARD, E3: P_CARD, H2: P_CARD,
            nearest(R, space): 2*P_CARD, nearest(U, space): P_CARD, space-3: P_CARD}
    if R1 in m:
        m[R1] += P_CARD
    else:
        m[R1] = P_CARD
    return m

def condense(arr):
    result = []
    for i in range(N):
        slice = arr[3*i:3*(i+1)]
        result.append(round(sum(slice), 5))
    return result

def spaces(start, end, step=1):
    return np.array(range(start, end, step)) % N

def nearest(arr, e):
    for a in arr:
        if a > e:
            return a
    return arr[0]

def enforce_G2J(moves):
    if G2J in moves:
        p = moves[G2J]
        del moves[G2J]
        moves[JAIL] = p

def state(space, doubles):
    return 3*space + doubles

if __name__ == "__main__":
    main()