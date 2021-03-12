def quickSort(nums, low, high):
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
        quicksort(nums, low, pivot - 1)
        quicksort(nums, pivot + 1, high)

    return nums
