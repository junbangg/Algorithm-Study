# Failed O(logn) binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[left] + numbers[mid] == target:
                return [left + 1, mid + 1]
            elif numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[mid] + numbers[right] == target:
                return [mid + 1, right + 1]
            elif numbers[mid] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[mid] < target:
                right -= 1
        return []

# Binary Search O(nlogn)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, value in enumerate(numbers):
            left, right = index + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                search = target - value
                if numbers[mid] < search:
                    left = mid + 1
                elif numbers[mid] > search:
                    right = mid - 1
                else:
                    return index + 1, mid + 1

# Two Pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left != right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1
