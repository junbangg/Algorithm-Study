def quickSort(nums, low, high, k):
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
        quickSort(nums, low, pivot - 1, k)
        quickSort(nums, pivot + 1, high, k)
        if k <= pivot or :
            return nums[k]
    #return nums


def kth(a, k):
    return quickSort(a, 0, len(a)-1, k-1)

nums = [43,41,64,23,34,64,2,1,9]
print(sorted(nums))
print(kth(nums, 4))
