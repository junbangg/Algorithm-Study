def solution(n, k, cmd):
    exists = [1] * n
    up = [-1] + [i for i in range(n-1)]
    down = [i for i in range(1, n)] + [-1]
    deleteStack = []

    def delete(index):
        exists[index] = 0
        deleteStack.append(index)
        if down[index] != -1:
            up[down[index]] = up[index]
        if up[index] != -1:
            down[up[index]] = down[index]
        nextIndex = down[index] if down[index] != -1 else up[index]

        return nextIndex

    def restore():
        restored = deleteStack.pop()
        if up[restored] != -1:
            down[up[restored]] = restored
        if down[restored] != -1:
            up[down[restored]] = restored
        exists[restored] = 1

    def goDown(index, moves):
        for _ in range(moves):
            index = down[index]
        return index

    def goUp(index, moves):
        for _ in range(moves):
            index = up[index]
        return index

    currentIndex = k
    for commandString in cmd:
        if commandString == 'C':
            currentIndex = delete(currentIndex)
        elif commandString == 'Z':
            restore()
        else: # move
            command, moves = commandString.split()
            if command == 'D':
                currentIndex = goDown(currentIndex, int(moves))
            else:
                currentIndex = goUp(currentIndex, int(moves))
    return ''.join(['O' if i else 'X' for i in exists])