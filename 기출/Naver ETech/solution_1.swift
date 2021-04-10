func solution(_ blocks : [Int]) -> Int {
    if blocks.count <= 1 {
        return 0
    }
    if blocks.count == 2 {
        return 2
    }
    var maxnum = 0
    for i in 0...blocks.count - 2 {
        var up = false
        var count = 1
        for j in i+1...blocks.count-1 {
            if up && blocks[j-1] > blocks[j] {
                break
            } else if blocks[j-1] < blocks[j] {
                up = true
            }
            count += 1
        }
        maxnum = max(maxnum, count)
    }
    return maxnum
}

var blocks = [2,4,3,1,5,6,7,4]
var blocks1 = [4,3,2,1,2,3,5,6,7,6,5,4,3,2,3,4]
solution(blocks)
