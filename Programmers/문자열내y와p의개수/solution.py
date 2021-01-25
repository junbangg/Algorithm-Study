def solution(s):
    p, y = 0, 0
    for i in s:
        if i.lower() == 'p': p += 1
        if i.lower() == 'y': y += 1
    if p != y: return False
    return True

#or

def solution(s):
    return s.lower().count('p') == s.lower().count('y')
