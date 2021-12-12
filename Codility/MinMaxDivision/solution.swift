import Foundation

func convertToPrefixSum(from array: [Int]) -> [Int] {
    var prefixSumArray = [array[0]]
    for i in 1..<array.count {
        prefixSumArray.append(prefixSumArray.last! + array[i])
    }
    return prefixSumArray
}

func getLargestSum(from array: [Int], with gap: Int) -> Int {
    var maxSum = -1
    for index in stride(from: gap, to: array.count, by: gap) {
        maxSum = max(maxSum, array[index])
    }
    return maxSum
}

public func solution(_ K : Int, _ M : Int, _ A : inout [Int]) -> Int {
    // write your code in Swift 4.2.1 (Linux)
    let prefixedArray = convertToPrefixSum(from: A)
    var answer = 0
    let left = 0
    let right = A.count
    while left <= right {
        let gap = left + (right - left) / 2
        let largestSum = getLargestSum(from: prefixedArray, with: gap)
        if largestSum >= answer {
            // 간격 줄이기
            right = gap - 1
        }
    }
    return 0
}


var arr = [2,1,5,1,2,2,2]
let K = 3
let M = 5

solution(3, 5, &arr)


