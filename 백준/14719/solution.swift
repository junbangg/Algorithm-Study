let W = readLine()!.split(separator: " ").compactMap{Int($0)}[1]
let nums = readLine()!.split(separator: " ").compactMap{Int($0)}

var left = 0
var right = W - 1
var leftMax = nums[0]
var rightMax = nums.last!
var answer = 0
while left <= right {
    leftMax = max(nums[left], leftMax)
    rightMax = max(nums[right], rightMax)
    if leftMax <= rightMax {
        answer += leftMax - nums[left]
        left += 1
    } else {
        answer += rightMax - nums[right]
        right -= 1
    }
}
print(answer)
