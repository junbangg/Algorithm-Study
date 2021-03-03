def solution(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        elif stack:
            stack.pop()
        else:
            return False
    return not stack
