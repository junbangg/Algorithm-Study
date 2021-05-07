import sys
import collections
def solution(gems):
    # length of unique gems(required)
    needs = len(set(gems))
    # save minimum size window
    answer = [sys.maxsize, [0,0]]
    # pointers
    left, right = 0, 0
    while right < len(gems) and left <= right:
        # check if current window contains all required gems
        cur = gems[left:right+1]
        contains = len(collections.Counter(set(cur)))
        #if gem is missing
        if needs != contains:
            right += 1
        #if all gems are in window
        else:
            # update answer to minimum sized window
            if len(cur) < answer[0]:
                answer = [len(cur), [left+1, right+1]]
            left += 1
    return answer[1]



gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

