def solution(number, k):
    s = []
    for i in range(len(number)):
        while s and k > 0 and s[-1] < number[i]:
            s.pop()
            k -= 1
        s.append(number[i])
    return ''.join(s[:len(number) - k])
