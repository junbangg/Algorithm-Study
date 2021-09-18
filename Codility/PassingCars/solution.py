def solution(A):
    prefix = [0] * len(A)
    ones = []
    for i in range(len(A)):
        if i > 0 and A[i] == 1:
            prefix[i] = prefix[i-1]
            ones.append(i)
        elif A[i] == 0:
            if i > 0:
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] += 1
    answer = 0
    for ind in ones:
        answer += prefix[ind]
    return answer if answer <= 1000000000 else -1
