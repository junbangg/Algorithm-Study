from collections import defaultdict
network = set()
def dfs(id, dic):
    if id not in network:
        network.add(id)
        for v in dic[id]:
            dfs(v, dic)


i = int(input())
dic = defaultdict(list)
for _ in range(i):
    a, b = input().split(' ')
    network.clear()
    dic[a].append(b)
    dic[b].append(a)
    # dfs
    dfs(a, dic)
    print(len(network))