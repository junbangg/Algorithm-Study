/**
 pivot 을 중앙값으로 설정을해서
 pivot을 기준으로 Array를 3개로 쪼갭니다. (filter 함수를 사용한 partition)
  재귀호출로 새로운 Array 만들기
 */

func quickSort<T: Comparable>(_ a: [T]) -> [T] {
    // edge case
    guard a.count > 1 else {return a}
    let pivot = a[a.count/2]
    let smaller = a.filter {$0 < pivot}
    let equal = a.filter {$0 == pivot}
    let bigger = a.filter {$0 > pivot}
    return quickSort(smaller) + equal + quickSort(bigger)
}

let list = [ 10, 0, 3, 9, 2, 14, 8, 27, 1, 5, 8, -1, 26 ]
quickSort(list)



/**
 Lomuto
1.  마지막 index 를 Pivot으로 설정을하고
2. 모든 원소에 대해서, Pivot 보다 작거나 같을 경우에 startIndex와 SWAP
3. startIndex 와 endIndex SWAP
 */
func partitionLomuto<T: Comparable>(_ a: inout [T], low: Int, high: Int) -> Int {
    let pivot = a[high]
    var i = low
    for j in low..<high {
        if a[j] <= pivot {
            a.swapAt(i, j)
            i += 1
        }
    }
    a.swapAt(i, high)
    return i
}
/**
 Recurse( startIndex ~ index-1)
 Recurse( index+1 ~ endIndex)
 */
func quickSortLomuto<T: Comparable>(_ a: inout [T], low: Int, high: Int) {
    if low < high {
        let p = partitionLomuto(&a, low: low, high: high)
        quickSortLomuto(&a, low: low, high: p - 1)
        quickSortLomuto(&a, low: p + 1, high: high)
    }
}
var nums = [ 10, 0, 3, 9, 2, 14, 26, 27, 1, 5, 8, -1, 8 ]
quickSortLomuto(&nums, low: 0, high: nums.count - 1)
print(nums)

