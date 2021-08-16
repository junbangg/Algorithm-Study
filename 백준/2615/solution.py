import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(19)]

def check(og_x, og_y, x, y, color, dir, count):
    # 오목일때, 양끝 기준으로 양방향으로 한번씩 더 검사를 해서 같은 색이면 6을 만들어준다
    if count == 5:
        if dir == 'NE':
            if 0 <= og_x + 1 < 19 and 0<= og_y - 1 < 19 and board[og_x + 1][og_y - 1] == color:
                count += 1
            elif 0 <= x-1 < 19 and 0 <= y + 1 < 19 and board[x-1][y+1] == color:
                count += 1
        elif dir == 'S':
            if 0 <= og_x - 1 < 19 and 0<= og_y < 19 and board[og_x - 1][og_y] == color:
                count += 1
            elif 0 <= x + 1 < 19 and 0 <= y < 19 and board[x+1][y] == color:
                count += 1
        elif dir == 'SE':
            if 0 <= og_x - 1 < 19 and 0<= og_y - 1 < 19 and board[og_x - 1][og_y - 1] == color:
                count += 1
            elif 0 <= x + 1 < 19 and 0 <= y + 1 < 19 and board[x + 1][y + 1] == color:
                count += 1
        elif dir == 'E':
            if 0 <= og_x < 19 and 0<= og_y - 1 < 19 and board[og_x][og_y - 1] == color:
                count += 1
            elif 0 <= x < 19 and 0 <= y + 1 < 19 and board[x][y + 1] == color:
                count += 1
        return count
    # 우상 / 하 / 우하 / 우  방향으로 탐색 
    if dir == 'NE':
        nx, ny = x-1, y+1
        if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            return check(og_x, og_y, nx, ny, color, dir, count+1)
    if dir == 'S':
        nx, ny = x+1, y
        if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            return check(og_x, og_y, nx, ny, color, dir, count+1)
    if dir == 'SE':
        nx, ny = x+1, y+1
        if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            return check(og_x, og_y, nx, ny, color, dir, count+1)
    if dir == 'E':
        nx, ny = x, y+1
        if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
            return check(og_x, og_y, nx, ny, color, dir, count+1)
    return count

for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] != 0:
            color = board[x][y]
            #NE
            a = check(x, y, x, y, color, 'NE', 1)
            #S
            b = check(x, y, x, y, color, 'S', 1)
            #SE
            c = check(x, y, x, y, color, 'SE', 1)
            #E
            d = check(x, y, x, y, color, 'E', 1)
            if a == 5 or b == 5 or c == 5 or d == 5:
                print(color)
                print(x+1, y+1)
                exit(0)
print(0)