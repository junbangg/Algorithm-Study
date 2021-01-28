def solution(n):
    return ''.join(list(map(lambda x: '수' if x %2==0 else '박', [i for i in range(n)])))
