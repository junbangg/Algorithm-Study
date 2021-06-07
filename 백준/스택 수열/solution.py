n = int(input())
count = 1
stack, output = [], []
for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        output.append('+')
        count += 1
    if stack[-1] == data:
        stack.pop()
        output.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(output))
