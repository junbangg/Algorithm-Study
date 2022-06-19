import sys

input = sys.stdin.readline

def solution(nums):
    stack = []
    answer = 0
    
    for newIndex, newHeight in enumerate(nums):
        startIndex = newIndex
        
        while stack and stack[-1][1] > newHeight:
            index, height = stack.pop()
            answer = max(answer, (newIndex-index)*height)
            startIndex = index
        stack.append([startIndex, newHeight])
    
    for index, height in stack:
        answer = max(answer, (len(nums)-index)*height)
    
    return answer
def largestRectangleArea(self, heights: List[int]) -> int:
    length = len(heights)
    leftSmaller = [0]*length
    rightSmaller = [length-1]*length

    stack = []

    # finding the left smaller for each height .
    for i in range(length):
        
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        
        if stack:
            leftSmaller[i] = 1 + stack[-1]
        
        stack.append(i)

    stack = []

    # finding the right smaller for each element
    for i in range(length-1,-1,-1):
        
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        
        if stack:
            rightSmaller[i] = stack[-1] - 1
        
        stack.append(i)

    # finding maximum area covered.
    maximumArea = float('-inf')
    for i in range(length):
        width = rightSmaller[i] - leftSmaller[i] + 1
        height = heights[i]
        area = width * height
        maximumArea = max(maximumArea, area)
    return maximumArea

while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break
    print(solution(nums))
