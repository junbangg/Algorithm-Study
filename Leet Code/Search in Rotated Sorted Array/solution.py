# First Attempt (Recursive)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right):
            mid = left + (right - left) // 2
            #mid = left + (right - left) // 2
            if left <= right:
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binarySearch(left, mid - 1)
                else:
                    return binarySearch(mid + 1, right)
            return -1
        left, right = 0, len(nums) - 1
        # Get pivot
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        a = binarySearch(0, left - 1)
        if a == -1:
            return binarySearch(left, len(nums) - 1)
        else:
            return a

# Iterative Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        # Get pivot
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)
            if nums[mid_pivot] == target:
                return mid_pivot
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
