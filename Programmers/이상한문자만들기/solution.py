def solution(s):
    answer = ''
    i = 0
    for c in s:
        if i % 2 == 0:
            answer += c.upper()
        if i % 2 == 1:
            answer += c.lower()
        if c == ' ':
            i = 0
        else:
            i += 1
    return answer

# or

def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
