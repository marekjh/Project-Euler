ranking = [str(n) for n in range(2, 10)]
ranking.extend(["T", "J", "Q", "K", "A"])

def main():
    with open("poker.txt", "r") as f:
        games = [x.strip().split() for x in f.readlines()]
    games = [(x[:5], x[5:]) for x in games]
    wins = 0
    for g in games:
        if p1_wins(g):
            wins += 1
    print(wins)

def p1_wins(game):
    player_1 = game[0]
    player_2 = game[1]
    outcomes = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight",
                "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
    type_1 = hand_type(player_1)
    type_2 = hand_type(player_2)
    p1 = outcomes.index(type_1[0])
    p2 = outcomes.index(type_2[0])
    if p1 > p2:
        return True
    if p1 < p2:
        return False
    p1_tie = type_1[1]
    p2_tie = type_2[1]
    for i in range(len(p1_tie)):
        if p1_tie[i] == p2_tie[i]:
            continue
        return p1_tie[i] > p2_tie[i]
        

def hand_type(hand):
    values = [ranking.index(card[0]) for card in hand]
    suits = [card[1] for card in hand]
    tiebreaker = sorted(list(set(values)), reverse=True)
    tiebreaker = sorted(tiebreaker, key=lambda v:values.count(v), reverse=True)

    cond1 = len(set(values)) == 5 and max(values) - min(values) == 4 #Straight
    cond2 = len(set(suits)) == 1 #Flush
    cond3 = sum(values) == 50 #Royal Flush
    conds = [cond1, cond2, cond3]
    if conds == [True, True, True]:
        return ("Royal Flush", tiebreaker)
    if conds[0:2] == [True, True]:
        return ("Straight Flush", tiebreaker)
    if conds[0]:
        return ("Straight", tiebreaker)
    if conds[1]:
        return ("Flush", tiebreaker)
    
    counts = sorted([values.count(v) for v in set(values)])
    if counts == [1, 4]:
        return ("Four of a Kind", tiebreaker)
    if counts == [2, 3]:
        return ("Full House", tiebreaker)
    if counts == [1, 1, 3]:
        return ("Three of a Kind", tiebreaker)
    if counts == [1, 2, 2]:
        return ("Two Pairs", tiebreaker)
    if counts == [1, 1, 1, 2]:
        return ("One Pair", tiebreaker)
    return ("High Card", tiebreaker)


main()