import Foundation

class Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        let nums = nums.sorted()
        var answer = Int.max
        var minimumDifference = Int.max
        
        for i in 0..<nums.count - 2 {
            var j = i  + 1
            var k = nums.count - 1
            
            while j < k {
                let total = nums[i] + nums[j] + nums[k]
                
                if total == target {
                    return target
                }
                if total < target {
                    j += 1
                } else {
                    k -= 1
                }
                let difference = abs(target - total)
                
                if difference < minimumDifference {
                    answer = total
                    minimumDifference = difference
                }
            }
        }
        return answer
    }
}