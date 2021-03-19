# Hoare 
def quickSort_hoare(nums, low, high):
    def partition(nums, pivot, high):
        left = pivot + 1
        right = high
        while True:
            while left < high and nums[left] < nums[pivot]:
                left += 1
            while right > pivot and nums[right] > nums[pivot]:
                right -= 1
            if right <= left:
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        nums[pivot], nums[right] = nums[right], nums[pivot]
        return right

    if low < high:
        pivot = partition(nums, low, high)
        quickSort_hoare(nums, low, pivot - 1)
        quickSort_hoare(nums, pivot + 1, high)
    return nums

# Lomuto 
def quickSort_lomuto(nums, low, high):
    def partition(low, high):
        pivot = nums[high]
        left = low
        for right in range(low, high):
            if nums[right] < pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        nums[left], nums[high] = nums[high], nums[left]
        return left

    if low < high:
        pivot = partition(low, high)
        quickSort_lomuto(nums, low, pivot - 1)
        quickSort_lomuto(nums, pivot + 1, high)

    return nums
nums = [4,3,2,2,3,1]
print(quickSort(nums, 0, len(nums)-1))
