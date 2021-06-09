n = int(input())
answer = []
for _ in range(n):
    s = input()
    left, right = [], []
    for c in s:
        if c == '>':
            if right:
                left.append(right.pop())
        elif c == '<':
            if left:
                right.append(left.pop())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)
    answer.append(''.join(left+right[::-1]))
for case in answer:
    print(case)
