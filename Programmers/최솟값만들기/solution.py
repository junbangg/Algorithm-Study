def solution(A,B):
    return sum(list(i[0] * i[1] for i in list(zip(sorted(A, reverse = True), sorted(B)))))

