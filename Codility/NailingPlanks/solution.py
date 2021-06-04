import collections, copy
def wrongsolution(A, B, C):
    # plank dic
    plankDic = collections.defaultdict(int)
    for i in range(len(A)):
        plankDic[(A[i], B[i])] = 0
    plankCount = len(plankDic)
    # nail dic to access plank dic
    nailDic = collections.defaultdict(list)
    for nail in C:
        for plank in plankDic.keys():
            if nail in [i for i in range(plank[0], plank[1]+1)]:
                nailDic[nail].append(plank)

    def check(num, pDic, pCount, nDic):
        for i in C[:num]:
            for plank in nDic[i]:
                if pDic[plank] == 0:
                    pCount -= 1
                pDic[plank] += 1
            if pCount == 0:
                return True
        return False
    # binarySearch 
    left, right = 1, len(A)
    answer = -1
    while left <= right:
        mid = left + (right - left) // 2
        # if all planks can be nailed with mid amount
        countCopy = plankCount
        if check(mid, copy.deepcopy(plankDic), countCopy, nailDic):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

def solution(A, B, C):
    def check(num):
        nails = [0] * 2*(len(C)+1)
        for nail in C[:num]:
            nails[nail] += 1
        for i in range(1, len(nails)):
            nails[i] += nails[i-1]
        for i in range(len(A)):
            if nails[B[i]] - nails[A[i]-1] == 0:
                return False
        return True
    # binarySearch 
    left, right = 1, len(A)
    answer = -1
    while left <= right:
        mid = left + (right - left) // 2
        # if all planks can be nailed with mid amount
        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


A = [1,4,5,8]
B = [4,5,9,10]
C = [4,6,7,10,2]
#C = [4,6,8,9,10]
'''
A = [1]
B = [3]
C = [1,2,3,4]
'''
print(solution(A,B,C))
