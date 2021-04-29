def solution(C, B):
    #limit = 5
    #target = 26
    def dfs(time, num):
        if num >= 200000 or num < 0 or time > limit:
            return
        if num == target:
            return True

        a = dfs(time+1, num*2)
        b = dfs(time+1, num+1)
        c = dfs(time+1, num-1)
        return a or b or c

    Clist = []
    for i in range(200000):
        C+=i
        Clist.append(C)
    answer = -1
    for limit, target in enumerate(Clist):
        if dfs(0, B):
            answer = limit
            break
    return answer




print(solution(11,2))
