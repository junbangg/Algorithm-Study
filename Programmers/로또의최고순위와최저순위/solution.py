# first attempt 
def solution(lottos, win_nums):
    dic = {6 : 1,
          5 : 2,
          4 : 3,
          3 : 4,
          2 : 5,
          1 : 6,
          0 : 6}
    # amount of zeros
    zeros = 0
    for num in lottos:
        if num == 0:
            zeros += 1
    # amount of common numbers
    match = len(set(lottos) & set(win_nums))
    # zeros + common numbers is the best possible match
    # common numbers is the worst possible match
    return dic[zeros + match], dic[match]


# refined
def solution(lottos, win_nums):
    dic = [6, 6, 5, 4, 3, 2, 1]
    zeros = lottos.count(0)
    match = len(set(lottos) & set(win_nums))
    return dic[zeros + match], dic[match]
