import sys
input = sys.stdin.readline
L, W, H = map(int, input().split())
N = int(input())
cubes = []
for _ in range(N):
    A, B = map(int, input().split())
    # cubes.append(((2**A)**3, B))
    cubes.append((2**A, B))
# cubes.sort(key = lambda x:x[0], reverse = True)
cubes.sort(reverse=True)

def divide(vol, i, cnt):
    if vol <= 0:
        if vol == 0:
            return cnt
        else:
            return -1
    cubeVal, cubeCount = cubes[i]
    validCubes = min(vol // cubeVal, cubeCount)
    return divide(vol - validCubes * cubeVal, i+1, cnt + validCubes)

print(cubes)
def fill(vol, l, w, h, i, cnt):
    if vol <= 0:
        if vol == 0:
            return cnt
        else:
            return -1
    smallestEdge = min(l, w, h)
    cubeVal, cubeCount = cubes[i]
    validCubes = 0
    if cubeVal <= smallestEdge:
        validCubes = min(cubeCount, smallestEdge)
        vol -= validCubes * (cubeVal ** 3)
    fill(vol, l, w, h - validCubes)
    fill(vol, l - validCubes, w, validCubes)
    fill(vol, validCubes, w - validCubes, validCubes)
    # return fill(vol, l, w, h, i+1, cnt + validCubes)



print(fill(L*W*H, L, W, H))