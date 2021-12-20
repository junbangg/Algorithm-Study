def solution(places):
    answer = []
    #dfs
    def dfs(grid, x, y, dist, valid):
        #base cases
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 'X':
            return
        #if node is 'P' and distance is less than 2-> not valid grid
        if grid[x][y] == 'P' and dist <= 2:
            valid = 0
            return valid
        grid[x][y] = 'X'
        # check node to visited
        # North
        dfs(grid, x-1, y, dist+1, valid)
        # South
        dfs(grid, x+1, y, dist+1, valid)
        # West
        dfs(grid, x, y+1, dist+1, valid)
        # East
        dfs(grid, x, y-1, dist+1, valid)
    # change to list map
    maps = []
    for place in places:
        temp = []
        for row in place:
            temp.append(list(row))
        maps.append(temp)
    # main function
    for grid in maps:
        #before = len(answer)
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 'P':
                    temp = []
                    temp.append(dfs(grid, x-1, y, 1, -1))
                    temp.append(dfs(grid, x+1, y, 1, -1))
                    temp.append(dfs(grid, x, y-1, 1, -1))
                    temp.append(dfs(grid, x, y+1, 1, -1))
                    if 0 in temp:
                        answer.append(1)
        # if nothing has been added to answer during recursion => grid is valid(append 1)
        if len(answer) == before:
            answer.append(1)
    return answer

def solution1(places):
    answer = []
    #dfs
    def dfs(grid, x, y, dist):
        #base cases
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        #if node is 'P' and distance is less than 2-> not valid grid
        if dist != 0 and grid[x][y] == 'P' and dist <= 2:
            answer.append(0)
            return
        elif dist != 0 and grid[x][y] == 'P':
            dist = 0
        # check node to visited
        grid[x][y] = 'X'
        # North
        dfs(grid, x-1, y, dist+1)
        # South
        dfs(grid, x+1, y, dist+1)
        # West
        dfs(grid, x, y+1, dist+1)
        # East
        dfs(grid, x, y-1, dist+1)
    # change to list map
    maps = []
    for place in places:
        temp = []
        for row in place:
            temp.append(list(row))
        maps.append(temp)
    # main function
    for grid in maps:
        before = len(answer)
        dfs(grid, 0, 0, 0)
        # if nothing has been added to answer during recursion => grid is valid(append 1)
        if len(answer) == before:
            answer.append(1)
    return answer




places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
