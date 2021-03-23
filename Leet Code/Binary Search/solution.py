class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # edge case
        if target not in nums:
            return -1
        def binarySearch(arr, low, high):
            mid = (low + high) // 2
            # base case
            if high >= low:
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    return binarySearch(arr, low, mid - 1)
                else:
                    return binarySearch(arr, mid + 1, high)
            else:
                return -1
        return binarySearch(nums, 0, len(nums))
