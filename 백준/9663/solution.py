import sys
input = sys.stdin.readline
N = int(input())


def checkCol(candidate, cur_col):
    if not candidate:
        return True
    cur_row = len(candidate)
    for prev_x, prev_y in enumerate(candidate):
        # same column
        if prev_y == cur_col or abs(prev_y - cur_col) == cur_row - prev_x:
            return False
    return True


def dfs(x, candidates, answers):
    if x == N:
        answers.append(candidates[:])
        return
    for y in range(N):
        # check if y is a valid place to place Queen
        if checkCol(candidates, y):
            candidates.append(y)
            dfs(x+1, candidates, answers)
            candidates.pop() # after dfs is done, no need to keep checking this collumn, so we pop and Prune

answers = []
dfs(0, [], answers)
print(len(answers))
