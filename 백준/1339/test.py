import sys, collections
input = sys.stdin.readline
N=int(input())

words = [input().rstrip() for _ in range(N)]

dic = collections.defaultdict(int)
for word in words:
  square_root = len(word) - 1
  for c in word:
    if dic[c] != 0:
      dic[c] += pow(10, square_root)
    else: 
      dic[c] = pow(10, square_root)
    square_root -= 1 

dic = sorted(dic.values(), reverse=True)
result, n = 0, 9
for value in dic:
  result += value * n
  n -= 1

print(result)