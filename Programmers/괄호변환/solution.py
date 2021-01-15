def solution(p):
    answer = ""
    if p == "": return answer
    o, c = 0, 0
    for c in p:
        if c == '(': o += 1
        else: c += 1

        if c == o: break
    u = p[c+o:]
    v = p[:c+o]

    if u[0] == '(':
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(': u[i] = ')'
            else: u[i] = '('

        for i in u:
            answer += u
    return answer


