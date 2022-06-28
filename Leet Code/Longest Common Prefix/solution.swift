// ["flower","flow","flight"]

// longestLength = 0
// 0~200 이진탐색

// prefix = strings[0][..<mid]

// for i in 1..<strs.length {
//     if 
// }

class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        var answer: String = ""
        var prefixString: String = ""
        var left: Int = 0
        var right: Int = 200
        
        first: while left <= right {
            let mid = left + (right - left) / 2
            
            if mid > strs[0].count {
                right = mid - 1
                continue
            }
            prefixString = String(strs[0].prefix(mid))
            for i in 1..<strs.count {
                if strs[i].count < mid {
                    right = mid - 1
                    continue first
                }
                if String(strs[i].prefix(mid)) != prefixString {
                    right = mid - 1
                    continue first
                }
            }
            answer = prefixString
            left = mid + 1
        }
        
        return answer
    }
}
