def solution(numbers, hand):
    answer = ''
    # grid in 2D array
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            ['*', 0, '#']]
    # coordination map
    # [ Hand data, [x,y] ]
    coords = {1: ['L', [0,0]],
              2: ['N', [0,1]],
              3: ['R', [0,2]],
              4: ['L', [1,0]],
              5: ['N', [1,1]],
              6: ['R', [1,2]],
              7: ['L', [2,0]],
              8: ['N', [2,1]],
              9: ['R', [2,2]],
              0: ['N', [3,1]] }
    # L R 
    L, R = [3, 0], [3, 2]
    for num in numbers:
        # if num is L or R designated
        h, pos = coords[num]
        if h == 'R':
            answer += 'R'
            R = pos
        elif h == 'L':
            answer += 'L'
            L = pos
        # if num is in the middle row
        else:
            distanceL = abs(L[0] - pos[0]) + abs(L[1] - pos[1])
            distanceR = abs(R[0] - pos[0]) + abs(R[1] - pos[1])
            if distanceL == distanceR:
                if hand == 'right':
                    answer += 'R'
                    R = pos
                else:
                    answer += 'L'
                    L = pos
            elif distanceL < distanceR:
                L = pos
                answer += 'L'
            else:
                R = pos
                answer += 'R'
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
print(solution(numbers, hand))
