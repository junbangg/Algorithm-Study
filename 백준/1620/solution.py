import sys
input = sys.stdin.readline
N, M = map(int, input().split())
mons, dic = [], {}
for i in range(N):
    mon = input().strip()
    dic[mon] = i + 1
    mons.append(mon)
for _  in range(M):
    cmd = input().strip()
    if cmd.isdigit():
        print(mons[int(cmd)-1])
    else:
        print(dic[cmd])