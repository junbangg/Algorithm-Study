class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []
        let parenMap: [Character: Character] = [
            ")": "(",
            "]": "[",
            "}": "{"
        ]
        
        for paren in s {
            if ["(","{","["].contains(paren) {
                stack.append(paren)
            } else if !stack.isEmpty && parenMap[paren] == stack.last {
                stack.removeLast()
            } else {
                return false
            }
        }
        
        return stack.isEmpty ? true : false
    }
}
