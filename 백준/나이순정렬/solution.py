n = int(input())
result = []
for i in range(n):
    age, name = input().split(' ')
    result.append([int(age), i, name])
result.sort(key = lambda x: (x[0], x[1]))
for item in result:
    print(''.join(str(item[0]) +' ' + item[2]))