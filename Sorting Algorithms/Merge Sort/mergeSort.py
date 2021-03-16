# Code for Merge Sort implementation
def mergeSort(arr):

    if len(arr) > 1:
        #find mid index
        mid = len(arr) / 2
        # (DIVIDE) the arr into 2 halves
        # first half
        L = arr[:mid]
        # second half
        R = arr[mid:]
        # sort first half
        mergeSort(L)
        # sort second half
        mergeSort(R)
        # (MERGE) Copy L and R data to arr
        i, j, k = 0, 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Check for remainders
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is")
    printList(arr)
