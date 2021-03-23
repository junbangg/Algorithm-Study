# Binary Search Implementation

def binarySearch(arr, low, high, x):
    mid = (low + high) // 2
    # base case
    if high >= low:
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1


arr = [1,5,6,8,9,11,14,15,17,18,20,26,28,43,46,52,60]
print(binarySearch(arr, 0, len(arr), 11))
