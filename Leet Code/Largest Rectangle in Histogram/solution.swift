/**
Test Case
[1, 1, 5, 1, 1, 1] -> 6
[2, 1, 5, 4, 2, 3] -> 8
[0] -> 0
**/
class Solution {
    func largestRectangleArea(_ heights: [Int]) -> Int {
        typealias Rectangle = (index: Int, height: Int)
        var stack: [Rectangle] = []
        var maxArea = 0 // len(height)
        var startIndex = 0
        
        for (i, currentHeight) in heights.enumerated() {
            startIndex = i
            while !stack.isEmpty && stack.last!.height > currentHeight {
                let rectangle = stack.removeLast()
                
                maxArea = max(maxArea, (i - rectangle.index) * rectangle.height)
                startIndex = rectangle.index
            }
            stack.append(Rectangle(index: startIndex, height: currentHeight))
        }
        
        for rectangle in stack {
            maxArea = max(maxArea, (heights.count - rectangle.index) * rectangle.height)
        }
        
        return maxArea
    }
}
