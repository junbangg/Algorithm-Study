import sys, itertools
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]

# 집이랑 치킨집 좌표 저장
ones, twos = [], []
for x in range(N):
    for y in range(N):
        if town[x][y] == 1:
            ones.append((x, y))
        elif town[x][y] == 2:
            twos.append((x, y))


answer = sys.maxsize
# 가능한 모든 M 개의 치킨집 조합 
for candidates in list(itertools.permutations(twos, M)):
    total = 0
    # 모든 집의 좌표
    for house_x, house_y in ones:
        closest = sys.maxsize
        # M 개의 치킨집과 집과의 거리의 최솟값 구하기
        for cand_x, cand_y in candidates:
            closest = min(closest, abs(house_x - cand_x) + abs(house_y - cand_y))
        total += closest
    # 최소 치킨거리 갱신
    answer = min(answer, total)
print(answer)

