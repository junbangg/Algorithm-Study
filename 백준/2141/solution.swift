func binarySearch(_ pref: [Int], _ nums: [(Int, Int)]) -> Int {
    var left = 0
    var right = pref.count - 1
    var answer = Int.max
    while left <= right {
        let mid = left + (right - left) / 2
        let leftSum = pref[mid]
        let rightSum = pref.last! - pref[mid]
        if (leftSum >= rightSum) {
            right = mid - 1
            answer = min(answer, nums[mid].0)
        }else {
            left = mid + 1
        }
        
    }
    return answer
}

let N = Int(readLine()!)!
var nums: [(Int, Int)] = []
for _ in 0..<N {
    let AB = readLine()!.split(separator: " ").compactMap{Int($0)}
    nums.append((AB[0], AB[1]))
}
nums.sort {
    $0.0 < $1.0
}
//누적합
var pref: [Int] = [nums[0].1]
for i in 1..<N {
    pref.append(pref[i-1] + nums[i].1)
}
// Solve
print(binarySearch(pref, nums))