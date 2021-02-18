def solution(A,B):
    return sum(i[0] * i[1] for i in zip(sorted(A, reverse = True), sorted(B)))
