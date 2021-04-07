import Foundation

// you can write to stdout for debugging purposes, e.g.
// print("this is a debug message")
public func solution(_ A : inout [Int]) -> Int {
    // write your code in Swift 4.2.1 (Linux)
    if A.count == 1 {
        return abs(A[0] * 2)
    }
    A.sort()
    var min = Int.max
    var left = 0
    var right = A.count - 1
    while left <= right {
        let sum = abs(A[left] + A[right])
        if sum == 0 {
            return sum
        }
        if sum < min {
            min = sum
        }
        if abs(A[left]) > abs(A[right]) {
            left += 1
        } else {
            right -= 1
        }
    }
    return min
}
