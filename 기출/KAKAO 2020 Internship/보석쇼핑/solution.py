from collections import defaultdict
def solution(gems):
    # answer
    answer = []
    minWindowSize = float('inf')

    # two pointer materials 
    uniqueGems = set(gems)
    gem_count = defaultdict(int)
    left = right = 0
    totalUniqueCount = len(uniqueGems)
    currentUniqueCount = 0
    
    # first position setup
    gem_count[gems[right]] += 1
    currentUniqueCount += 1
    if currentUniqueCount == totalUniqueCount:
        answer = [left, right]
        left = right = 1
        gem_count[gems[right]] -= 1
    else:
        right += 1

    # two pointer
    while left <= right and right < len(gems):
        if gem_count[gems[right]] == 0: # new gem    
            currentUniqueCount += 1
        # window <- gem
        gem_count[gems[right]] += 1
        # check unique
        if currentUniqueCount == totalUniqueCount:
            # left 이동
            while left < right and gem_count[gems[left]] > 1:
                gem_count[gems[left]] -= 1
                left += 1
            currentWindowSize = right - left
            if currentWindowSize < minWindowSize:
                minWindowSize = currentWindowSize
                answer = [left, right]
            elif right - left == minWindowSize:
                if answer and left < answer[0]:
                    answer = [left, right]
        right += 1
    return answer[0]+1, answer[1]+1