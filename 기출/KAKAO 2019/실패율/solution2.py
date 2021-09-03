# 1 실패율 구하기
#   - 도전 자 수 (N 이상의 수)
#   - 실패 자 수 (N 이하 의 수)
#   - 나누기

# 2 실패율: stage 번호 저장

# 3 실패율 정렬 (Reverse)

# 4 [ 실패율에 맞는 stage 번호 ] 리턴
def solution(N, stages):
    
    data = {} # {stage 번호: 실패율 }
    attempts = len(stages)
    for stage in range(1, N+1):
        # 도전자
        if attempts > 0:
            fail = stages.count(stage)
            data[stage] = fail / attempts
            attempts -= fail
        else:
            data[stage] = 0
    answer = sorted(data, key = lambda x: data[x], reverse = True)
    
    return answer

# N = 6
# stages = [2, 1, 2, 5, 2, 4, 3, 3]
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
