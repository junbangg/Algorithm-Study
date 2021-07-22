import sys, collections
input = sys.stdin.readline

visited = []
def dfs(ind, comb):
    global answer
    if comb in visited:
        return 
    if ind < len(categories):
        for item in dic[categories[ind]]:
            answer += 1
            nxt = comb[:]
            nxt.append(item)
            visited.append(nxt)
            dfs(ind+1, nxt)


tc = int(input())

for _ in range(tc):
    N = int(input())
    dic = collections.defaultdict(list)
    for _ in range(N):
        item, category = input().split()
        dic[category].append(item)

    categories = list(dic.keys())
    visited.clear()
    answer = 0
    dfs(0, [])
    print(answer)






