def solution(n, k, cmd):
    exists = [1] * n
    up = [-1] + [i for i in range(n-1)]
    down = [i for i in range(1, n)] + [-1]
    deleteStack = []

    def delete(index):
        exists[index] = 0
        deleteStack.append(index)
        nextIndex = down[index]
        if index == n - 1:
            nextIndex = up[index]
        up[down[index]] = up[index]
        down[up[index]] = down[index]

        return nextIndex

    def restore():
        restored = deleteStack.pop()
        up[down[restored]] = restored
        down[up[restored]] = restored
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