from collections import deque
n, m = map(int, list(input().split(' ')))
first, second = list(input().split(' '))
# dictionary
dic = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1,
        'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2,
        'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}
# combine and convert to int
combine = deque()
i, j = 0, 0
while i < len(first) and j < len(second):
    combine.append(dic[first[i]])
    combine.append(dic[second[j]])
    i += 1
    j += 1
while i < len(first):
    combine.append(dic[first[i]])
    i += 1
while j < len(second):
    combine.append(dic[second[j]])
    j += 1
# calculate
while len(combine) > 2:
    prev = combine[0]
    for i in range(1,len(combine)):
        temp = combine[i]
        combine[i] = (combine[i] + prev) % 10
        prev = temp
    combine.popleft()
if combine[0] == 0:
    combine.popleft()
print(''.join(list(map(str, combine))) + '%')