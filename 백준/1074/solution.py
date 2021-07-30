import sys
input = sys.stdin.readline
N, R, C = map(int, input().split())
def divide(x, y, size):
    global answer
    if x == R and y == C:
        print(answer)
        exit(0)
    if size == 1:
        answer += 1
        return
    if not x <= R < x + size and not y <= C < y + size:
        answer += size * size
        return
    divide(x, y, size//2)
    divide(x, y + size//2, size//2)
    divide(x+size//2, y, size//2)
    divide(x+size//2, y+size//2, size//2)
answer = 0
divide(0, 0, 2**N)