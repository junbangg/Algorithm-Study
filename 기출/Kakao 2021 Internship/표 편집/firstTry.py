from gettext import find


def solution(n, k, cmd):
    answer = ['O'] * n
    parents = {}
    for i in range(n):
        parents[i] = [i, i]
    deleteStack = []

    def findDown(parents, a):
        if parents[a][0] != a:
            parents[a][0] = findDown(parents, parents[a][0])
        return parents[a][0]

    def unionDown(parents, a, b):
        aParent = findDown(parents, a)
        bParent = findDown(parents, b)
        if aParent < bParent:
            parents[aParent][0] = bParent
        else:
            parents[bParent][0] = aParent

    def findUp(parents, a):
        if parents[a][1] != a:
            parents[a][1] = findUp(parents, parents[a][1])
        return parents[a][1]

    def unionUp(parents, a, b):
        aParent = findUp(parents, a)
        bParent = findUp(parents, b)
        if aParent <= bParent:
            parents[bParent][1] = aParent
        else:
            parents[aParent][1] = bParent

    def goUp(index, moves):
        currentIndex = index
        for _ in range(moves):
            parent = findUp(parents, currentIndex)
            # print("------parent------", parent)
            if parent == currentIndex:
                unionUp(parents, currentIndex-1, currentIndex)
                parent = findUp(parents, currentIndex-1)
            else:
                unionUp(parents, parent, currentIndex)
                parent = findUp(parents, parent)
            currentIndex = parent
            # print("--------new index-------", parent)
        return currentIndex

    def goDown(index, moves):
        currentIndex = index
        for _ in range(moves):
            # if currentIndex == n-1:
            #     currentIndex = goUp(currentIndex, 1)
            # else:
            parent = findDown(parents, currentIndex)
            if parent == currentIndex:
                unionDown(parents, currentIndex, currentIndex + 1)
                parent = findDown(parents, currentIndex)
            else:
                unionDown(parents, currentIndex, parent)
            currentIndex = parent
        return currentIndex

    def delete(index):
        # deleteStack.append(index)
        # answer[index] = 'X'
        # if index == 0:
        #     pass
        # elif index == n - 1:
        #     pass
        # else:
        #     upIndex = findUp(parents, index)
        #     downIndex = findDown(parents, index)
        #     if upIndex == index:
        #         pass
        #     if downIndex == index:
        #         unionDown(index, downIndex)
        #         pass

        pass
        # return newIndex

    def restore():
        pass

    currentIndex = k
    # for commandString in cmd:
    #     if commandString == 'C':
    #         delete()
    #         pass
    #     elif commandString == 'Z':
    #         restore()
    #         pass
    #     else: # move
    #         command, moves = commandString.split()
    #         if command == 'D':
    #             currentIndex = goDown(currentIndex, int(moves))
    #             pass
    #         else:
    #             currentIndex = goUp(currentIndex, int(moves))
    #             pass
    currentIndex = goDown(currentIndex, 2)
    currentIndex = goUp(currentIndex, 3)
    print(currentIndex)
    print(parents)
    currentIndex = goDown(currentIndex, 4)
    print(currentIndex)
    print(parents)
    # currentIndex = delete(currentIndex)
    # print(currentIndex)
    # print(parents)
    return ""

n = 8
k = 2
cmd = ["D 2", "C","U 3","C","D 4","C","U 2","Z","Z"]
solution(n, k, cmd)
