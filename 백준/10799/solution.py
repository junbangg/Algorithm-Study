parens = list(input())
count = 0
stack, prev = [], ''
for p in parens:
    if p == '(':
        stack.append('(')
    else:
        if prev == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
    prev = p
print(count)
