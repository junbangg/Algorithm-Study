# 1-0 Knapsack Problem
cargo = [(4, 12),
         (2, 1),
         (10, 4),
         (1,1),
         (2,2) ]
capacity = 15

def knapsack(cargo, capacity):
    sack = []
    for i in range(len(cargo) + 1):
        sack.append([])
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                sack[i].append(0)
            elif cargo[i - 1][1] <= j:
                # max value 
                sack[i].append(max(cargo[i-1][0] + sack[i-1][j - cargo[i-1][1]],
                                   sack[i-1][j]))
            else:
                sack[i].append(sack[i-1][j])
    return sack[-1][-1]

a = knapsack(cargo, capacity)
print(a)
