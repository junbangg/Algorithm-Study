n, m = map(int, list(input().split(' ')))
A, B = list(input().split(' '))
# dictionary
dic = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1,
        'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2,
        'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}
# combine names
AB = ''    
minLen = min(len(A), len(B))
for i in range(minLen):
    AB += A[i] + B[i]
AB += A[minLen:] + B[minLen:]
# convert to numbers
lst = [dic[i] for i in AB]
# calculate
for i in range(n + m - 2):
    for j in range(n + m - 1 - i):
        lst[j] += lst[j+1]
print('{}%'.format(lst[0] % 10*10 + lst[1] % 10))