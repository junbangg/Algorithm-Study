def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    return s[(len(s)//2) - 1] + s[(len(s)//2)]
#or
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]
