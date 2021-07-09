import sys
input = sys.stdin.readline

N = int(input())
if N <= 3:
    print(N)
    exit(0)
a, b = 1, 2
for _ in range(N-1):
    a, b = b, (a+b) % 15746
print(a)