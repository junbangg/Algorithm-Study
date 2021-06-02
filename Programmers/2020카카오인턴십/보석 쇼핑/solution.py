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
    # add first gem to dic
    dic[gems[0]] += 1
    contains += 1
    #pointers
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

# Second attempt
import collections
def solution(gems):
    counter = collections.defaultdict(int)
    need = len(set(gems))
    left, right = 0, 0
    minLength = len(gems) + 1
    answer = []
    while right < len(gems):
        if counter[gems[right]] == 0:
            need -= 1
        counter[gems[right]] += 1
        if need == 0:
            while left < right:
                if counter[gems[left]] > 1:
                    counter[gems[left]] -= 1
                    left += 1
                else:
                    break
            if minLength > right - left + 1:
                minLength = right - left + 1
                answer = [left+1, right+1]
        right += 1
    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))






import sys, collections
def solution(gems):
    dic = {}                                     #gem의 개수를 기록 하기위한 dictionary
    for gem in set(gems):
        dic[gem] = 0
    needs = len(set(gems))                       #필요한 고유 gem의 개수 
    contains = 0                                 #현재 Window안에 있는 gem의 개수
    answer = [sys.maxsize, [0,0]]                 #최소 크기 window 의 인덱스를 저장 할 배열
    dic[gems[0]] += 1        #포인터가 0부터 시작하니까 우선 dic에 첫번째 gem에 대해 increment
    contains += 1
    left, right = 0, 0        #포인터
    while right < len(gems) and left <= right:
        if contains == needs:            #현 window에 모든 gem이 들어있을 경우
            if right-left+1 < answer[0]:   #최소 window size 유지하면서 정답 배열 update
                answer = [right-left+1, [left+1, right+1]]
            dic[gems[left]] -= 1.       #left 포인터가 증가하면 그 인덱스의 gem은 dic에서 -1
                               #빠져나간 gem이 dic에서 0이 됐으면 contains 에서도 -1 을 해준다
            if dic[gems[left]] == 0:
                contains -= 1
            left += 1          #포인터 이동
        # 부족한 gem 이 있으면
        else:
            right += 1.           #포인터 이동
            if right < len(gems):      # 인덱스 오류 피하기
                               # Window에 새롭게 추가될 gem이 dic에 없던거면 contains + 1해준다
                if dic[gems[right]] == 0:
                    contains += 1
                dic[gems[right]] += 1
    return answer[1] 
