def calculateMoves(queue, left, right):
    end = len(queue)
    half = end // 2
    moves = 0
    # 1 조건
    if left < half and right < half:
        moves += right # 첫번째 큐 포인터 부분 전부 이동
        moves += half # 두번째 큐 전부 이동
        moves += left # 첫번째 큐 앞 부분 다시 이동
        return moves
    # 2 조건
    if left < half and half <= right < end:
        moves += left
        moves += right - half
        return moves
    # 3 조건
    if half <= left < end and half <= right < end:
        moves += half # 첫번째 큐 전부 두번째 큐 뒤로 이동
        moves += (left - half) * 2 # 두번째 큐에서 이동 할 앞 부분 두 번 이동
        moves += right - left  # 두 번째 큐 에서 첫번째 큐로 이동
        return moves

def getMinimumMoves(firstQueue, secondQueue, target):
    queue = firstQueue + secondQueue
    queueSize = len(queue)
    minMoves = float('inf')

    for left in range(1, queueSize-1):
        total = 0

        for right in range(left + 1, queueSize):
            total += queue[right-1]
            if total == target:
                minMoves = min(minMoves, calculateMoves(queue, left, right))
    return -1 if minMoves == float('inf') else minMoves

def solution(queue1, queue2):
    queue1Total = sum(queue1)
    queue2Total = sum(queue2)
    target = (queue1Total + queue2Total) // 2
    # edge case
    if queue1Total == target:
        return 0

    minimumMoves = getMinimumMoves(queue1, queue2, target)
    return minimumMoves

# tc1 = [3,2,7,2,4,6,5,1]
# left = 1
# right = 3
# left = 3
# right = 6
# left = 5
# right = 7
# print(calculateMoves(tc1, left, right))
# queue1 = [3, 2, 7, 2]
# queue2 = [4, 6, 5, 1]

# queue1 = [1, 2, 1, 2]	
# queue2 = [1, 10, 1, 2]
queue1 = [1, 1]
queue2 = [1, 5]

print(solution(queue1, queue2))

# a = [1,2,3,4,5]
# print(a[:2])
# print(a[1:4])
# [1, 2]
