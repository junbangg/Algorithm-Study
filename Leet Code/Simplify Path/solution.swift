class Solution {
    func simplifyPath(_ path: String) -> String {
        var stack: [String] = []
        
        for subPath in path.split(separator: "/") {
            if subPath == "." {
                continue
            } else if subPath == ".." {
                if !stack.isEmpty {
                    stack.removeLast()
                }
            } else {
                stack.append(String(subPath))
            }
        }

        return "/\(stack.joined(separator: "/"))"
    }
}
