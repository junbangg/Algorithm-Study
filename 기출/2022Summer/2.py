def getManhattanDistance(x1, y1, x2, y2):
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance

def getOptimal(L, R, targetX, targetY):
    x1, y1 = L[0], L[1]
    x2, y2 = R[0], R[1]
    leftDistance = getManhattanDistance(x1, y1, targetX, targetY)
    rightDistance = getManhattanDistance(x2, y2, targetX, targetY)
    if leftDistance < rightDistance:
        return 'L'
    if rightDistance < leftDistance:
        return 'R'
    else:
        leftRowDistance = abs(y1 - targetY)
        rightRowDistance = abs(y2 - targetY)
        if leftRowDistance < rightRowDistance:
            return 'L'
        if rightRowDistance < leftRowDistance:
            return 'R'
        else:
            if targetY <= 4:
                return 'L'
            else:
                return 'R'

def solution(line):
    keyboard = {
        '1': [0, 0], '2': [0, 1], '3': [0, 2], '4': [0, 3], '5': [0, 4], '6': [0, 5], '7': [0, 6], '8': [0, 7], '9': [0, 8], '0': [0, 9],
        'Q': [1, 0], 'W': [1, 1], 'E': [1, 2], 'R': [1, 3], 'T': [1, 4], 'Y': [1, 5], 'U': [1, 6], 'I': [1, 7], 'O': [1, 8],'P': [1, 9]
    }
    answer = []
    L = [1, 0]
    R = [1, 9]
    for target in line:
        targetX, targetY = keyboard[target][0], keyboard[target][1]
        optimal = getOptimal(L, R, targetX, targetY)
        if optimal == 'L':
            answer.append(0)
            L[0], L[1] = targetX, targetY
        else:
            answer.append(1)
            R[0], R[1] = targetX, targetY

    return answer

tc = "RYI76"
print(solution(tc))