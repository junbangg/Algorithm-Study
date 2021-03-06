# heapq solution
import sys, heapq, collections
input = sys.stdin.readline
h = []
dic = collections.defaultdict(int)
N = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    dic[tree] += 1
    N += 1

for tree, cnt in dic.items():
    heapq.heappush(h, (tree, cnt))

while h:
    tree, cnt = heapq.heappop(h)
    print('%s %.4f' %(tree, cnt/N*100))