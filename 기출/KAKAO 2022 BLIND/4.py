
# 1. 어피치 n 발 -> 라이언 n 발
# 2. 점수 계산
#     - if a >= b:
#         apeach += k
#     - else:
#         ryan += k

# if apeach > = ryan:
    # apeach wins


def solution(n, info):

    winningIndexes = [i+1 for i in info]
    candidates = []
    def subset_sum(positions, target, partial=[0]*len(info)):
        s = sum(partial)

        # check if the partial sum is equals to target
        if s == target: 
            candidates.append(partial)
            return
        if s >= target:
            return  # if we reach the number why bother to continue

        for i in range(len(positions)):
            n = positions[i]
            remaining = positions[i+1:]
            partial_copy = partial[:]
            partial_copy[n] = winningIndexes[n]
            subset_sum(remaining, target, partial_copy)
    subset_sum([i for i in range(11)], n)
    answer = []
    maxWin = -1
    score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    alternates = []
    for ryans_arrows in candidates:
        apeach = ryan = 0
        for i in range(len(info)):
            if info[i] < ryans_arrows[i]:
                ryan += score[i]
            elif info[i] != 0:
                apeach += score[i]
        if ryan > apeach:
            if maxWin < ryan:
                answer = ryans_arrows
                maxWin = ryan
            if maxWin == ryan:
                alternates.append([ryan, ryans_arrows])
    for score, arrows in alternates:
        if score == maxWin:
            answer_sum = alternate_sum = 0
            for i in range(len(arrows)):
                answer_sum += i * answer[i]
                alternate_sum += i * arrows[i]
            if alternate_sum < answer_sum:
                answer = arrows


    # print(maxWin)
    # print(answer)
    return answer if answer else [maxWin]
    # return candidates


tc1 =[5, [2,1,1,1,0,0,0,0,0,0,0]]
tc2 = [1, [1,0,0,0,0,0,0,0,0,0,0]]
tc3 = [9, [0,0,1,2,0,1,1,1,1,1,1]]
tc4 = [10, [0,0,0,0,0,0,0,0,3,4,3]]
# 6+4 = 10


print(solution(tc4[0], tc4[1]))