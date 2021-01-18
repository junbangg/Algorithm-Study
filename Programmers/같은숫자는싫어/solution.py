def solution(arr):
    answer = []
    prev = -1
    for i in arr:
        if i is not prev:
            answer.append(i)
            prev = i
    return answer

#or

def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
