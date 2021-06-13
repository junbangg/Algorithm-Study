# 11650
n = int(input())
result = []
for _ in range(n):
    x, y = input().split(' ')
    result.append((int(x), int(y)))
result.sort(key = lambda x: (x[0], x[1]))
for pt in result:
    print(''.join(str(pt[0]) + ' ' + str(pt[1])))


