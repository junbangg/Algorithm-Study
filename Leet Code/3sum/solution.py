# Too slow
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cands = [sorted(c) for c in map(list, itertools.combinations(nums, 3)) if sum(c) == 0]
        return set(map(tuple, cands))

# Brute Force Solution  O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    temp = [nums[i], nums[j], nums[k]]
                    if sum(temp) == 0 and temp not in answers:
                        answers.append(temp)
        return answers
# Brute Force Solution(Book) O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]:continue
            for j in range(i+1, len(nums)-1):
                if j>i+1 and nums[j] == nums[j-1]:continue
                for k in range(j+1, len(nums)):
                    if k>j+1 and nums[k] == nums[k-1]:continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        answers.append([nums[i], nums[j], nums[k]])
        return answers
# Two Pointer Solution(mine)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]: continue
            left, right = i+1, len(nums) - 1  #check
            while left<right:
                temp = [nums[i], nums[left], nums[right]]
                if sum(temp) == 0 and temp not in answers:
                    answers.append(temp)
                    left +=1
                    right -= 1
                elif sum(temp) < 0:
                    left += 1
                else:
                    right -= 1
        return answers
# Two Pointer Solution (optimized)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]: continue
            left, right = i+1, len(nums) - 1
            while left<right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    answers.append([nums[i], nums[left], nums[right]])
                    # skip past duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answers
