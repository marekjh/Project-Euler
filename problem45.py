def find_t():
    tn = 286
    pn = 166
    hn = 144
    p = []
    h = []

    while True:
        p.append(pn * (3 * pn - 1) / 2)
        h.append(hn * (2 * hn - 1))
        t_current = tn * (tn + 1) / 2
        if t_current in p and t_current in h:
            return t_current
        tn += 1
        pn += 1
        hn += 1

print(find_t())