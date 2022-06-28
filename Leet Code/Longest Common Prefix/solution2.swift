class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        var answer: String = ""
        let minLengthString = strs.min { $0.count < $1.count }
        guard var minLengthString = minLengthString else {
            return ""
        }
        var i: Int = 0
        
        while minLengthString != "" && i < strs.count {
            if !strs[i].starts(with: minLengthString) {
                minLengthString = String(minLengthString.dropLast())
            } else {
                i += 1
            }
        }
        
        return minLengthString
    }
}
