import sys, collections
input = sys.stdin.readline

S, P = map(int, input().split())
randomString = input().rstrip()
requiredDic = collections.defaultdict(int)
requiredDic['A'], requiredDic['C'], requiredDic['G'], requiredDic['T'] = map(int, input().split())

targetsLeft = 0
for val in requiredDic.values():
    if val >= 1: targetsLeft += 1

currentDic = collections.defaultdict(int)
for i in range(P):
    currentDic[randomString[i]] += 1
    if requiredDic[randomString[i]] > 0 and requiredDic[randomString[i]] == currentDic[randomString[i]]:
        targetsLeft -= 1
        
answer = 0
if targetsLeft == 0:
    answer += 1
    
left, right = 0, P - 1
while right < S - 1:
    # left
    oldLeft = randomString[left]
    if requiredDic[oldLeft] > 0 and requiredDic[oldLeft] == currentDic[oldLeft]:
        targetsLeft += 1
    currentDic[oldLeft] -= 1
    left += 1
    # right
    right += 1
    newRight = randomString[right]
    currentDic[newRight] += 1
    if requiredDic[newRight] > 0 and requiredDic[newRight] == currentDic[newRight]:
        targetsLeft -= 1
        
    if targetsLeft == 0:
        answer += 1
print(answer)