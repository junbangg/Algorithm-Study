N = int(input())
M = int(input())
S = input()
p = 'I'
for _ in range(N):
    p += 'OI'

i = count = 0
window = len(p)
while i < M:
    if S[i:i+window] == p:
        count += 1
    i += 1
print(count)
