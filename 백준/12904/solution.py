import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
    exit(0)
else:
    print(0)
