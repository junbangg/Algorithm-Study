import Foundation

// Input
let ns = readLine()!.split(separator: " ").compactMap{Int($0)}
let nums = readLine()!.split(separator: " ").compactMap{Int($0)}
let N = ns[0]
let S = ns[1]

// DFS
func dfs(ind : Int, total : Int) {
    if (total == S) {
        answer += 1
    }
    if (ind >= N) {
        return
    }
    for i in ind+1..<N {
        dfs(ind: i, total: total + nums[i])
    }
    
}

var answer = 0
for i in 0..<N {
    dfs(ind: i, total: nums[i])
}
print(answer)

