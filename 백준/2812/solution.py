import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = list(input().rstrip())

ptr = 1
switch = False
while ptr < len(num):
    while ptr > 0 and num[ptr-1] < num[ptr]:
        num.pop(ptr-1)
        ptr -= 1
        K -= 1
        if K == 0:
            switch = True
            break
    if switch:
        break
    ptr += 1
print(int(''.join(num)))