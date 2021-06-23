def solution(dirs):
    answer = 0
    visited = []
    move = {'U': [-1, 0],
            'D': [1, 0],
            'L': [0, -1],
            'R': [0, 1]}
    x, y = 5, 5
    for c in dirs:
        dx, dy = x + move[c][0], y + move[c][1]
        if dx >= 0 and dx < 11 and dy >= 0 and dy < 11:
            if [(x, y), (dx, dy)] not in visited and [(dx, dy), (x, y)] not in visited:
                answer += 1
            visited.append([(x,y), (dx, dy)])
            visited.append([(dx, dy), (x, y)])
            x, y = dx, dy
    return answer