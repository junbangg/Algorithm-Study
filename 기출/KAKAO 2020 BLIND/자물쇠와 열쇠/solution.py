def isValid(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        elif stack:
            stack.pop()
        else:
            return False
    return True

def solution(p):
    if not p:
        return p
    if isValid(p):
        return p
    # split into u, v
    openCount = closedCount = 0
    for i in range(len(p)):
        if p[i] == '(':
            openCount += 1
        else:
            closedCount += 1
        if openCount == closedCount:
            break
    u = p[:i+1]
    v = p[i+1:]
    if isValid(u):
        return u + solution(v)
    else:
        u = u[1:-1]
        temp = '(' + solution(v) + ')'
        for c in u:
            if c == "(":
                temp += ")"
            else:
                temp += "("
        return temp

    
tc1 = "(()())()"
tc2 = ")("
tc3 = "()))((()"
tc4 = "(()()))("
tc5 = "))))(((("

print(solution(tc3))