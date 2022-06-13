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
        
        var currentState: Bool? = nil
        var wiggleCount = 0
        
        for i in 1..<nums.count {
            if nums[i] == nums[i-1] {
                continue
            }
            let isPositive = nums[i] - nums[i-1] > 0
            
            if isPositive == currentState {
                continue
            } else {
                currentState = isPositive
                wiggleCount += 1
            }
        }
        
        return wiggleCount + 1
    }
}
