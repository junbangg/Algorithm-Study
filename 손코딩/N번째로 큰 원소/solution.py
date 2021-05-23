def quickSort(nums, low, high, count, k):

    def partition(nums, low, high):
        left, pivot = low, nums[high]
        for right in range(low, high):
            if nums[right] > pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        nums[left], nums[high] = nums[high], nums[left]
        return left

    if low<high:
        p = partition(nums, low, high)
        quickSort(nums, low, p-1)
        quickSort(nums, p+1, high)
    return nums


nums = [4,3,5,3,12,3,2,4,9]
k = 3
print(quickSort(nums, 0, len(nums)-1))
