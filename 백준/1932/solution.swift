import Foundation

let N = readLine()!.split(separator: " ").compactMap { Int($0) }.first!
var dp: [[Int]] = []

for _ in 0..<N {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    dp.append(input)
}

for i in 1..<N {
    for j in 0..<dp[i].count {
        if j == 0 {
            dp[i][j] += dp[i-1][j]
        } else if i == j {
            dp[i][j] += dp[i-1][j-1]
        } else {
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
        }
    }
}
print(dp[N-1].max()!)

