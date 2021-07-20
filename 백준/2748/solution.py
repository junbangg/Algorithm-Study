import sys
input = sys.stdin.readline
a, b = 0, 1
for _ in range(int(input())-1):
    a, b = b, a+b
print(b)
