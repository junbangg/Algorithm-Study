import sys
sys.setrecursionlimit(10**5)
k = int(sys.stdin.readline())

def recurse(n):
    if n <= 1:
        return n
    elif n % 2 == 0:
        return recurse(n//2)
    else:
        return 1 - recurse(n//2)

#print(recurse(k-1))
# or
print(bin(k-1).count('1')%2)
