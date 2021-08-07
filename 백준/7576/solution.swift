import Foundation
//Solution
func solution(_ graph: [[Int]], _ m: Int, _ n: Int) -> Int {
    // 준비물: visited, queue, bfs
    var visited = [[Int]]


    //first traversal (count tomatos) .. 에외처리



}
//Input
let NM = readLine()!.split(separator: " ").compactMap{Int($0)}
let N = NM[0]
let M = NM[1]
var grid = [[Int]]()
for _ in 0..<M {
    let nums = readLine()!.split(separator: " ").compactMap{Int($0)}
    grid.append(nums)
}
// Solve

