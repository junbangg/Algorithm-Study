class Solution {
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {
        var answer = Array(repeating: 0, count: temperatures.count)
        var stack: [Int] = []
        
        for (index, temperature) in temperatures.enumerated() {
            while !stack.isEmpty && temperature > temperatures[stack.last!] {
                let lastIndex = stack.popLast()!
                
                answer[lastIndex] = index - lastIndex
            }
            
            stack.append(index)
        }
        
        return answer
    }
}
