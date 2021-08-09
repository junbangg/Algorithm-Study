let N = Int(readLine()!)!
let nums = readLine()!.split(separator: " ").compactMap{Int($0)}
var dp = [Int](repeating: 1, count: N)
var answer = 0

func dfs(_ ind: Int) {
    for i in ind+1..<N {
        if (nums[ind] < nums[i]) {
            dp[i] = max(dp[ind]+1, dp[i])
            answer = max(dp[i], answer)
            dfs(i)
        }
    }
}
for i in 0..<N {
    dfs(i)
}
print(answer)