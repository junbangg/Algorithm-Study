def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [55,2,3,4,23,56,23,4,33]
print(bubbleSort(nums))
