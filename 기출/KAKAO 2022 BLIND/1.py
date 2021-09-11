# 충분히 이해하고 풀기
# 비효율적인 방법이라도 떠오르면 그것부터 구현해보기
# 제출하기 전에 충분히 예외 케이스 생각해보기


# 각 유저는 한 번에 한명의 유저 신고 가능
# 한명이 다른 사람을 여러번 신고해도 1회로 처리됨
# 

# 신고한 사람 -> : 누구를 신고했는지 기록
# -> 신고 당한 사람  :  몇 번 신고 당했는지 기록(똑같은 사람한테 당한건 1회로 처리)
#     - 자기 신고 한 사람
#     - 몇 번 당했는지 

# reporter = {'muzi': [frodo, neo],
#             apeach: [frodo, muzi],
#             frodo: [neo] }

# reported = {frodo: [2, [muzi, apeach]],
#             neo: [2, [muzi, frodo]],
#             muzi: [1, [apeach],}

# answer = [0] * len(id_list)
# for key in reporter:
#     if reported[key][0] > k:
#         banned.append(key)
# for b in banned:
#     for key in reporter:
#         if b in reporter[key]:
#             answer[key] += 1
from collections import defaultdict
def solution(id_list, report, k):
    reporter_data = defaultdict(set)
    reported_data = {}
    
    for data in report:
        reporter, reported = data.split()
        reporter_data[reporter].add(reported)
        if reported in reported_data:
            if reporter not in reported_data[reported][1]:
                reported_data[reported][1].append(reporter)
                reported_data[reported][0] += 1
        else:
            reported_data[reported] = [1, [reporter]]
    
    answer = [0] * len(id_list)

    for reporter in reporter_data:
        for reported in reporter_data[reporter]:
            if reported_data[reported][0] >= k:
                answer[id_list.index(reporter)] += 1
    
    return answer

# ids = ["muzi", "frodo", "apeach", "neo"]
ids = ["con", "ryan"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(ids, report, k))