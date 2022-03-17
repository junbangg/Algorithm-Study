class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var anagrams: [String: [String]] = [:]
        
        for string in strs {
            let key = string.map { String($0) }.sorted(by: {
                $0 < $1
            }).joined()
            
            if anagrams[key] != nil {
                anagrams[key]!.append(string)
            } else {
                anagrams[key] = [string]
            }
        }
        
        return Array(anagrams.values)
    }
}
