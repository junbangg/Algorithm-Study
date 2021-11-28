import sys, itertools
input = sys.stdin.readline

possibleGames = list(itertools.combinations([0,1,2,3,4,5], 2))
def dfs(count):
    global result, wins, draws, losses
    if count == 15:
        if wins.count(0) == 6 and draws.count(0) == 6 and losses.count(0) == 6:
            result = 1
        return
    x, y = possibleGames[count]
    if wins[x] > 0 and losses[y] > 0:
        wins[x] -= 1
        losses[y] -= 1
        dfs(count + 1)
        wins[x] += 1
        losses[y] += 1
    if wins[y] > 0 and losses[x] > 0:
        wins[y] -= 1
        losses[x] -= 1
        dfs(count + 1)
        wins[y] += 1
        losses[x] += 1
    if draws[x] > 0 and draws[y] > 0:
        draws[x] -= 1
        draws[y] -= 1
        dfs(count + 1)
        draws[x] += 1
        draws[y] += 1

answer = []
for _ in range(4):
    data = list(map(int, input().split()))
    wins, draws, losses = [], [], []
    for i, v in enumerate(data):
        if i % 3 == 0:
            wins.append(v)
        elif i % 3 == 1:
            draws.append(v)
        else:
            losses.append(v)
    result = 0
    dfs(0)
    answer.append(result)
    
print(*answer)

        

    
