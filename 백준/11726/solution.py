import sys
input = sys.stdin.readline
N = int(input())
if N <= 2:
    print(N)
    exit(0)
a, b = 1, 2
for i in range(2, N):
    a, b = b, a + b
print(b%10007)