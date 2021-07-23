import sys, collections
input = sys.stdin.readline

def dfs(comb, ind, C, dic, categories):
    global answer, visited
    if ind < C:
        for cloth in dic[categories[ind]]:
            comb.append(cloth)
            print(comb)
            if comb not in visited:
                visited.append(comb)
                answer += 1
                dfs(comb, ind+1, C, dic, categories)
                comb.pop()

tc = int(input())
for _ in range(tc):
    N = int(input())
    dic = collections.defaultdict(list)
    for _ in range(N):
        item, category = input().split()
        dic[category].append(item)

    categories = list(dic.keys())
    C = len(categories)
    visited = []
    #dfs
    answer = 0
    dfs([], 0, C, dic, categories)
    print(visited)
    print(answer)






