// Test Cases
// [2, 1] -> 2
// [1, 2] -> 2
// [1, 1] -> 1
// [1] -> 1
// missed case
// [3, 3, 3, 2, 5]
class Solution {
    func wiggleMaxLength(_ nums: [Int]) -> Int {
        //edge case
        if nums.count == 1 {
            return nums.count
        }
        
        var currentState = nums[1] - nums[0] > 0
        var wiggleCount = nums[1] != nums[0] ? 1 : 0
        
        for i in 2..<nums.count {
            let isPositive = nums[i] - nums[i-1] > 0
            
            if nums[i] == nums[i-1] || isPositive == currentState {
                continue
            } else {
                currentState = isPositive
                wiggleCount += 1
            }
        }
        
        return wiggleCount + 1
    }
}
