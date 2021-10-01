import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
length, width, height = map(int, input().rstrip().split(" "))
n = int(input().rstrip())
cubes = [0] * 21
for _ in range(n):
    a, b = map(int, input().rstrip().split(" "))
    cubes[a] += b

total = 0
count = 0
for i in range(19, -1, -1):
    total <<= 3
    t = min(cubes[i], (length >> i)*(width >> i)*(height >> i) - total)
    total += t
    count += t

if(total == length*width*height):
    print(count)
else:
    print(-1)
