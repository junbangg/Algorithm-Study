# 1 실패율 구하기
#   - 도전 자 수 (N 이상의 수)
#   - 실패 자 수 (N 이하 의 수)
#   - 나누기

# 2 실패율: stage 번호 저장

# 3 실패율 정렬 (Reverse)

# 4 [ 실패율에 맞는 stage 번호 ] 리턴
def solution(N, stages):
    stage_failRate = {}
    attempts = len(stages)
    for stage in range(1, N+1):
        if attempts > 0:
            fail = stages.count(stage)
            stage_failRate[stage] = fail / attempts
            attempts -= fail
        else:
            stage_failRate[stage] = 0
    return sorted(stage_failRate, key = lambda x: stage_failRate[x], reverse = True)

# N = 6
# stages = [2, 1, 2, 5, 2, 4, 3, 3]
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
