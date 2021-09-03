# 1 실패율 구하기
#   - 도전 자 수 (N 이상의 수)
#   - 실패 자 수 (N 이하 의 수)
#   - 나누기

# 2 실패율: stage 번호 저장

# 3 실패율 정렬 (Reverse)

# 4 [ 실패율에 맞는 stage 번호 ] 리턴
from collections import defaultdict
def solution(N, stages):
    
    # 1 실패율 구하기
    data = defaultdict(list) # {실패율: [stage 번호] }
    rates = []
    for stage in range(1, N+1):
        # 도전자
        attempt = 0
        attempters = []
        for s in stages:
            if s >= stage:
                attempt += 1
                attempters.append(s)
        fails = 0
        for a in attempters:
            if a <= stage:
                fails += 1
        # 실패율 저장
        rate = 0
        if attempt > 0:
            rate = fails / attempt
        data[rate].append(stage)
        data[rate].sort(reverse=True)
        rates.append(rate)
    
    # sort rate
    rates.sort(reverse=True)
    answer = []
    print(rates)
    print(data)
    for r in rates:
        answer.append(data[r].pop())
        # while data[r]:
            # answer.append(heapq.heappop(data[r]))
    
    return answer

# N = 6
# stages = [2, 1, 2, 5, 2, 4, 3, 3]
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
