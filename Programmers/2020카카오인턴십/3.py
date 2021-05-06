import collections
def solution(gems):
    required = set(gems)
    checkRequired = sorted(list(required))
    need = collections.Counter(required)
    missing = len(required)
    left = start = end = 0
    for right, gem in enumerate(gems, 1):
        missing -= need[gem] > 0
        need[gem] -= 1
        if missing == 0:
            while left < right and need[gems[left]] < 0:
                need[gems[left]] += 1
                left += 1
            if not end or right - left <= end - start:
                start, end = left, right
                need[gems[left]] += 1
                missing += 1
                left += 1
        if sorted(list(set(gems[start:end+1]))) == checkRequired:
            return [start, end]
    return [start, end]

