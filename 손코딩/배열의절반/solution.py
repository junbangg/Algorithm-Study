input = [2, 7, 7, 7, 1, 7, 2]
half = 3
2 : 2
7 : 4
1 : 1

# First Attempt  O(n)
def returnIfCountIsHalf(nums):
    # half length
    half = len(nums) // 2
    # count elements 
    dic = {}
    for n in nums:
        if not nums[n]:
            nums[n] = 1
        else:
            nums[n] += 1
    for key in dic:
        if dic[key] > half:
            return key
    return -1


input = [2, 4, 3, 3, 3, 5, 3, 3, 2]
half = 4.5

2:1
4:1
3:3
5:1

3-> if dic[3] > half: return

# O(n)
def optimizedSolution(nums):
    half = len(nums) / 2
    dic = {}
    for n in nums:
        if not dic[n]:
            dic[n] = 1
        else:
            dic[n] += 1
        # check for answer
        if dic[n] > half:
            return n
    return -1
