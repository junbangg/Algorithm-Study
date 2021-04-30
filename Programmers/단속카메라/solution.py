def solution(routes):
    routes.sort(key = lambda x: x[0], reverse = True)
    answer, start, end = 0, 0, 0
    while routes:
        start, end = routes.pop()
        while start < end and routes:
            if routes[-1][0] == start:
                end = routes.pop()[1]
            start += 1
        answer += 1
    return answer
