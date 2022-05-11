class Solution {
    func jump(_ nums: [Int]) -> Int {
        var count = 0
        var currentMax = 0
        var nextMax = 0
        
        for i in 0..<nums.count-1 {
            nextMax = max(nextMax, i + nums[i])
            
            if i == currentMax {
                currentMax = nextMax
                count += 1
            }
        }
        return count
    }
}
