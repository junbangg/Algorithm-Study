import sys, collections
input = sys.stdin.readline
N, K = map(int, input().split())
num = collections.deque((input().rstrip()))
stack = []
while num:
    while stack and stack[-1] < num[0] and K > 0:
        stack.pop()
        K -= 1
    stack.append(num.popleft())
# K 를 아직 다 안썼을때에 대한 예외처리
if K != 0:
    stack = stack[:-K]
print(int(''.join(stack)))