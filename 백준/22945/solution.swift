import Foundation

let N = Int(readLine()!)
let numbers = readLine()!.split(separator: " ").compactMap { Int($0) }

var left = 0
var right = numbers.count - 1
var answer = 0
var total = 0

while left < right {
    total = min(numbers[left], numbers[right]) * (right - left - 1)
    answer = max(answer, total)
    if numbers[left] <= numbers[right] {
        left += 1
    } else {
        right -= 1
    }
}

print(answer)