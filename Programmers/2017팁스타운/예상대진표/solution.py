def solution(n, a, b):
    round = 0
    while a != b:
        round += 1
        a, b = (a + 1) // 2, (b + 1) // 2
    return round

    