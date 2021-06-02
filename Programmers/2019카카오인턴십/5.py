def solution(k, room_number):
    answer, slots, stack = [0] * len(room_number), [False] * (k+1), [i for i in range(k, 0, -1)]
    for ind, num in enumerate(room_number):
        if not slots[num]:
            answer[ind] = num
            slots[num] = True
            if num == stack[-1]:
                stack.pop()
        else:
            nextSlot = num
            while slots[nextSlot]:
                nextSlot = stack.pop()
            answer[ind] = nextSlot
            slots[nextSlot] = True
    return answer


k = 10
nums = [1,3,4,1,3,1]
print(solution(k, nums))
