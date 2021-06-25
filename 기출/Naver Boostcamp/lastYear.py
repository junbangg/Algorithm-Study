from collections import Counter
def solution(arr):
    answer = []
    dic = Counter(arr)
    for val in dic.values():
        if val > 1:
            answer.append(val)
    return answer if answer else [-1]
print(solution([1, 2, 3, 3, 3, 3, 4, 4]))
print(solution([3,2,4,4,2,5,2,5,5]))
print(solution([3,5,7,9,1]))