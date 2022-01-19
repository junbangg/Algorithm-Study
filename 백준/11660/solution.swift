import Foundation

func solution(grid: [[Int]], x1: Int, y1: Int, x2: Int, y2: Int) -> Int {
    if x1 == x2 && y1 == y2 {
        return grid[x2][y2] - grid[x2-1][y2] - grid[x2][y2-1] + grid[x2-1][y2-1]
    }
    let left = grid[x2][y1 - 1]
    let right = grid[x1 - 1][y2]
    let mid = grid[x1 - 1][y1 - 1]
    
    return grid[x2][y2] - left - right + mid
}

let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NM[0]
let M = NM[1]
var grid: [[Int]] = []
grid.append(Array(repeating: 0, count: N + 1))

(0..<N).forEach { _ in
    let arr = readLine()!.split(separator: " ").compactMap { Int($0) }
    grid.append([0] + arr)
}
// 누적합
for x in 1..<N+1 {
    for y in 1..<N+1 {
        grid[x][y] += grid[x][y-1] + grid[x-1][y] - grid[x-1][y-1]
    }
}
(0..<M).forEach { _ in
    let coords = readLine()!.split(separator: " ").compactMap { Int($0) }
    print(solution(grid: grid, x1: coords[0], y1: coords[1], x2: coords[2], y2: coords[3]))
}


