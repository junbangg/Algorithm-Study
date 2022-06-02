import Foundation

func createNodeDictionary(with edges: [[Int]]) -> [Int: [Int]] {
    var nodes: [Int: [Int]] = [:]
    
    for pair in edges {
        nodes[pair[0], default: []].append(pair[1])
        nodes[pair[1], default: []].append(pair[0])
    }
    
    return nodes
}

func solution(_ n:Int, _ edge:[[Int]]) -> Int {
    var nodes = createNodeDictionary(with: edge)
    var distances = Array(repeating: Int.max, count: n+1)
    var dp = Array(repeating: 0, count: n+1)
    var q: [Int] = [1]
    var maxDistance = 0
    var pointer = 0
    
    distances[1] = 0
    
    while pointer < q.count {
        let current = q[pointer]
        
        for next in nodes[current]! {
            if distances[current] + 1 < distances[next] {
                distances[next] = distances[current] + 1
                maxDistance = max(maxDistance, distances[next])
                dp[distances[next]] += 1
                q.append(next)
            }
        }
        pointer += 1
    }
    return dp[maxDistance]
}
