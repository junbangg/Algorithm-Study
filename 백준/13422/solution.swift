import Foundation

func solution(houses: [Int], N: Int, M: Int, K: Int) -> Int {
    var currentSum = houses[0..<M].reduce(0, +)
    var answer = currentSum < K ? 1 : 0
    if N == M {
        return answer
    }
    var left = 1
    var right = M
    
    while left < N {
        currentSum -= houses[left - 1]
        currentSum += houses[right % N]
        if currentSum < K {
            answer += 1
        }
        left += 1
        right += 1
    }
    
    return answer
}

let T = Int(readLine()!)!

for _ in 0..<T {
    let NMK = readLine()!.split(separator: " ").compactMap { Int($0) }
    let N = NMK[0]
    let M = NMK[1]
    let K = NMK[2]
    let houses = readLine()!.split(separator: " ").compactMap { Int($0) }
    
    print(solution(houses: houses, N: N, M: M, K: K))
}


