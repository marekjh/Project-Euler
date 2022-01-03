def maximized_triangle(n):
    pythagorean_triplets = []
    for a in range(1, n + 1):
        end = a
        if n - a < end:
            end = n - a
        for b in range(1, end + 1):
            c = (a ** 2 + b ** 2) ** 0.5
            if str(c).endswith(".0"):
                pythagorean_triplets.append((a, b, c))
    
    p_dict = {}
    for triple in pythagorean_triplets:
        p = sum(triple)
        if p <= 1000:
            if p in p_dict:
                p_dict[p] += 1
            else:
                p_dict[p] = 1
    
    return max(p_dict.items(), key=lambda item: item[1])[0]

print(maximized_triangle(1000))
            
        
        

#https://projecteuler.net/problem=39