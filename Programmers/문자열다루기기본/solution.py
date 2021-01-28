def solution(s):
    return s == ''.join([c for c in s if c.isnumeric()]) and len(s) in (4,6)


def solution(s):
    return s.isdigit() and len(s) in (4,6)

