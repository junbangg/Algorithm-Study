import UIKit

/**
 Merge Sort
 1. 분할
 2. 정복하면서 정렬
 */

func mergeSort(_ a: [Int]) -> [Int] {
    //  base case
    guard a.count > 1 else {return a}
    // mid
    let mid = a.count / 2
    // left
    let left = mergeSort(Array(a[0..<mid]))
    //right
    let right = mergeSort(Array(a[mid..<a.count]))
    //merge
    return merge(leftArray: left, rightArray: right)
}


func merge(leftArray: [Int], rightArray: [Int]) -> [Int] {
    // merge into one array
    var mergedArray = [Int]()
    var left = 0
    var right = 0
    while left < leftArray.count && right < rightArray.count {
        //compare left element and right element and add smaller to mergedArray
        if leftArray[left] <= rightArray[right] {
            mergedArray.append(leftArray[left])
            left += 1
        }else {
            mergedArray.append(rightArray[right])
            right += 1
        }
    }
    // append remainder of left array
    while left < leftArray.count {
        mergedArray.append(leftArray[left])
        left += 1
    }
    // append remainder of right array
    while right < rightArray.count {
        mergedArray.append(rightArray[right])
        right += 1
    }
    //return merged array
    return mergedArray
}

var testCase = [2,12,4,3243,23,2,45,3,12,-21,3,2,-3,0]
print(mergeSort(testCase))
