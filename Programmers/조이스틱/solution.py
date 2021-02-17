# first try
def solution(name):
    codes = list(map(ord, name))
    # Change to list of indexes that are not 'A'
    ind = list(i for i, j in enumerate(list(name)) if j != 'A')
    # variables
    i, answer, fwd, back = 0, 0, 0, 0
    end_flag = False
    l_name = len(name)
    while ind:
        cur = ind[i]
        letter = codes[cur]
        if letter <= 78: answer += letter - 65
        else: answer += 91 - letter
        if len(ind) == 1: fwd, back = 0, 0
        else:
        # i 뒤 타겟과의 거리
            if i == 0:
                back = l_name - ind[-1]
                end_flag = True
            else:
                back = ind[i-1]
            # i 앞 타겟 과의 거리
            if i == len(ind) - 1:
                fwd = ind[0] + 1
            if i < len(ind) - 1:
                fwd = ind[i+1] - cur
        # 비교
        if back < fwd:
            answer += back
            ind.remove(cur)
            if end_flag:
                i = len(ind) - 1
                end_flag = False
            else:
                i -= 1
        else:
            answer += fwd
            ind.remove(cur)
    return answer

# Answer
def solution(name):
    codes = list(map(ord, name))
    i, answer, fwd, back = 0, 0, 0, 0
    end_flag = False
    l_name = len(name)
    # A 아닌 index 로 list 생성
    ind = list(i for i, j in enumerate(list(name)) if j != 'A')
    while ind:
        cur = ind[i]
        letter = codes[cur]
        if letter <= 78: answer += letter - 65
        else: answer += 91 - letter
        if len(ind) == 1: fwd, back = 0, 0
        else:
        # i 뒤 타겟과의 거리
            if i == 0:
                back = cur + 1
                end_flag = True
            else:
                back = cur - ind[i-1]
            # i 앞 타겟 과의 거리
            if i == len(ind) - 1:
                fwd = ind[0] + 1
            if i < len(ind) - 1:
                fwd = ind[i+1] - cur
        # 비교
        if back < fwd or cur == l_name - 1:
            answer += back
            ind.remove(cur)
            if end_flag:
                i = len(ind) - 1
                end_flag = False
            else:
                i -= 1
        else:
            answer += fwd
            ind.remove(cur)
    return answer
