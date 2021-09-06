from itertools import combinations
def solution(relation):
    answer = 0
    relation = list(map(list,zip(*relation)))
    rows = [i for i in range(len(relation))]
    candidates, combs = [], []
    # 모든 가능한 후보키 조합 생성
    for i in range(1, len(relation) + 1):
        for comb in list(combinations(rows, i)):
            combs.append(comb)
    # 모든 조합에 대한 최소성, 유일성 체크
    for comb in combs:
        # 최소성 체크
        flag = False
        for cand in candidates:
            for c in combinations(comb, len(cand)):
                if c == cand:
                    flag = True
                    break
        if flag:
            continue
        # 유일성 체크
        check = []
        for col in range(len(relation[0])):
            tup = ()
            for row in comb:
                tup += (relation[row][col], )
            check.append(tup)
        if len(check) == len(set(check)):
            candidates.append(comb)
            answer += 1
    # print('candidates', candidates)
    return answer