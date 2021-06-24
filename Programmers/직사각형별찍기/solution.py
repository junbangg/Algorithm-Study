a, b = map(int, input().strip().split(' '))
for _ in range(b):
    temp = []
    for _ in range(a):
        temp.append('*')
    print(''.join(temp))

# alternate solution
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
