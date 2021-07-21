# sort solution
import sys, collections
input = sys.stdin.readline
trees = []
dic = collections.defaultdict(int)
N = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    dic[tree] += 1
    N += 1

for tree, cnt in dic.items():
    trees.append((tree, cnt))

trees.sort(reverse=True)
while trees:
    tree, cnt = trees.pop()
    print('%s %.4f' %(tree, cnt/N*100))