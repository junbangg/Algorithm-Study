def insertionSortForVersion(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

def insertionSortWhileVersion(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        i += 1
    return arr

test = [6,5,4,3,2,1]
print(insertionSortWhileVersion(test))
