import numpy as np
from collections import Counter

N = 40
D = 4

GO = 0
V_JAIL = 10
IN_JAIL = 40
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

DEPTH = 10000000

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
    ranking = sorted([x for x in enumerate(result)], key=lambda k: k[1], reverse=True)
    print("".join(2*str(x[0]) if x[0] < 10 else str(x[0]) for x in ranking[:3]))
    # print(condense(result))
    # print(sorted([x for x in enumerate(result)], key=lambda k: k[1], reverse=True))

def transition(si, di):
    t = []
    m0, m1 = roll_moveset(si)
    f0, f1 = full_moveset(m0), full_moveset(m1)
    for sf in range(N):
        t.extend(to_add(si, di, sf, f0, f1))
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
        return {space: 14*P_CARD, GO: P_CARD, IN_JAIL: P_CARD}
    m = {space: 6*P_CARD, GO: P_CARD, IN_JAIL: P_CARD, C1: P_CARD, E3: P_CARD, H2: P_CARD,
            nearest(R, space): 2*P_CARD, nearest(U, space): P_CARD, space-3: P_CARD}
    if R1 in m:
        m[R1] += P_CARD
    else:
        m[R1] = P_CARD
    return m

def to_add(si, di, sf, m0, m1):
    p0, p1 = m0.get(sf, 0), m1.get(sf, 0)
    j0, j1 = m0.get(IN_JAIL, 0), m1.get(IN_JAIL, 0)
    add_if_jail = [j0+j1, j0+j1, j0+1/D]
    if di == 0:
        add = [p0, p1, 0]
    elif di == 1:
        add = [p0, 0, p1]
    else:
        add = [p0, 0, 0]
    if sf == V_JAIL:
        add[0] += add_if_jail[di]
    return add

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
        moves[IN_JAIL] = p

if __name__ == "__main__":
    main()