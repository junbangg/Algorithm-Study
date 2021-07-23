import sys
input = sys.stdin.readline


tc = int(input())
for _ in range(tc):
    N = int(input())
    dic = {}
    for _ in range(N):
        item, category = input().split()
        if category in dic:
            dic[category].append(item)
        else:
            dic[category] = [item, 'nothing']
    answer = 1
    for key in list(dic.keys()):
        answer *= len(dic[key])
    print(answer - 1)




