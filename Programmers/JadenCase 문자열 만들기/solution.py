def solution(s):
    s = list(s)
    prev = ''
    for i in range(len(s)):
        if prev == ' ' or i == 0:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
        prev = s[i]
    return ''.join(s)
