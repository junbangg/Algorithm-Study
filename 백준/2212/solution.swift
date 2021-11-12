import Foundation
let N = Int(readLine()!)!
let K = Int(readLine()!)!
var nums = readLine()!.split(separator: " ").compactMap{ Int($0) }

if K >= N {
    print(0)
    exit(0)
}

nums.sort()
var distances: [Int] = []
for i in 1..<nums.count {
    distances.append(nums[i] - nums[i-1])
}

distances.sort { $0 > $1 }
for _ in 0..<K-1 {
    distances.removeFirst()
}
print(distances.reduce(0, +))