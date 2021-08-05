import sys
input = sys.stdin.readline
N = int(input())
find = int(input())

# 출력용
grid = [[0 for _ in range(N)] for _ in range(N)]
ans_x, ans_y = 0, 0
# 남 -> 동 -> 북 -> 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

number, distance = N*N, N
# 첫 N 개 숫자 채우기 (1열)
for i in range(distance):
    grid[i][0] = number 
    if number == find:
        ans_x, ans_y = i+1, 1 
    number -= 1
distance -= 1

#시작 정보
x, y, direction = i, 0, 1
while distance > 0:
    # 2번 돌리고나서 distance 를 줄여준다
    for _ in range(2):
        # distance 만큼 돌려준다
        for _ in range(distance):
            x += dx[direction]
            y += dy[direction]
            grid[x][y] = number
            if number == find:#찾으라고 한 숫자 찾으면 정답 좌표 저장
                ans_x, ans_y = x+1, y+1
            number -= 1
        direction = (direction+1) % 4 #남, 동, 북, 서 순서대로 이동
    distance -= 1
for i in range(N):
    print(*grid[i])
print(ans_x, ans_y)