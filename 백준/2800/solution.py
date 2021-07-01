from collections import deque
pars = list(input())
#1 get index pairs
temp = deque()
noPars = ''
for i, v in enumerate(pars):
    if v in '()':
        temp.append(i)
    else:
        noPars += v
pairs = []
while temp:
    pairs.append((temp.popleft(), temp.pop()))

answer = set()
# start with -1
def recurse(exp, pair, i):
    if ''.join(exp) == noPars:
        return
    o, c = pair
    if o >= 0 and c >= 0:
        exp.pop(c-i)
        exp.pop(o-i)
        answer.add(''.join(exp))

    for i in range(i+1, len(pairs)):
        recurse(exp, pairs[i], i+1)
    return

recurse(pars, (-1, -1), -1)
print(answer)
