//Binary Search

/**
 1. 분할 정복 알고리즘
 2. 탐색 할 target 을 mid 값과 비교하면서, mid 값의 왼쪽에 있는지 오른쪽에 있는지 추측하면서 재귀호출
 
 - Parameters:
 - a: input array
 - target: target
 - Returns: index of target
 */

/// Iterative
func binarySearchIterative<T: Comparable>(_ a: [T], target: T) -> Int? {
    var left = 0
    var right = a.count - 1
    
    while left <= right {
        let mid = left + (right - left) / 2
        if a[mid] == target {
            return mid
        } else if a[mid] < target {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return nil
}

/// Recursive
func binarySearchRecursive<T: Comparable>(_ a: [T], low: Int, high: Int, target: T) -> Int? {
    let mid = low + (high - low) / 2
    // base case
    if low <= high {
        if a[mid] == target {
            return mid
        } else if a[mid] < target {
            binarySearchRecursive(a, low: low, high: mid - 1, target: target)
        } else{
            binarySearchRecursive(a, low: mid + 1, high: high, target: target)
        }
    }
    return nil
}


var testCase3 = [1,54,34,23,45,23,4,23,4,53,2,34,2,1,2,3,0,3,-2]
quickSort(testCase3)
print(testCase3)
let index = binarySearchRecursive(testCase3,low: 0, high: testCase3.count - 1, target: 53)
print(testCase3[index!])

