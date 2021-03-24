# Pythonic Solution
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# Without using the comforts of Python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        nums2.sort()
        for i in nums1:
            left, right = 0, len(nums2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] == i:
                    answer.add(i)
                    break
                elif nums2[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1
        return answer

# Binary Search with library function
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        nums2.sort()
        for i in nums1:
            index = bisect.bisect_left(nums2, i)
            if len(nums2) > 0 and index < len(nums2) and i == nums2[index]:
                answer.add(nums2[index])
        return answer

# Two Pointer Solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                answer.add(nums1[i])
                i += 1
                j += 1
        return answer
