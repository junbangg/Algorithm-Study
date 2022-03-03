def solution(routes):
    routes.sort(key = lambda x: x[1])
    answer = 1
    endMax = routes[0][1]
    for start, end in routes:
        if start <= endMax or end <= endMax:
            continue
        answer += 1
        endMax = end

    return answer
