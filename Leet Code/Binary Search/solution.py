# Recursive Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(low, high):
            mid = (low + high) // 2
            # base case
            if high >= low:
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binarySearch(low, mid - 1)
                else:
                    return binarySearch(mid + 1, high)
            else:
                return -1
        return binarySearch(0, len(nums)-1)

# Iterative Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
