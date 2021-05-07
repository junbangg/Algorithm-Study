import sys, collections
def solution(gems):
    # dic for required gems
    dic = {}
    for gem in set(gems):
        dic[gem] = 0
    # length of unique gems(required)
    needs = len(set(gems))
    contains = 0
    # save minimum size window [window size, [startIndex, endIndex]]
    answer = [sys.maxsize, [0,0]]
    # pointers
    dic[gems[0]] += 1
    contains += 1
    left, right = 0, 0
    while right < len(gems) and left <= right:
        # if current window contains all required gems
        if contains == needs:
            # update minimum window
            if right-left+1 < answer[0]:
                answer = [right-left+1, [left+1, right+1]]
            # decrement gem from dic
            dic[gems[left]] -= 1
            #if amount of decremented gem is 0..decrement from contain 
            if dic[gems[left]] == 0:
                contains -= 1
            # move pointer
            left += 1
        #if gem is missing
        else:
            # move pointer
            right += 1
            # check for index out of reach
            if right < len(gems):
                # if next gem is a new update to dic..increment to contain
                if dic[gems[right]] == 0:
                    contains += 1
                dic[gems[right]] += 1
    return answer[1] 


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

