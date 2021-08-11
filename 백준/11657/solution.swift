typealias Data = (cur: Int, nxt: Int, weight: Int)
let NM = readLine()!.split(separator: " ").compactMap{Int($0)}
let N = NM[0]
let M = NM[1]
var edges: [Data] = []
for _ in 0..<M {
    let abc = readLine()!.split(separator: " ").compactMap{Int($0)}
    edges.append((abc[0], abc[1], abc[2]))
}
let INF = Int.max
var dist = [Int](repeating: INF, count: N+1)

func bellmanFord(_ src: Int) -> Bool {
    dist[src] = 0
    for i in 0..<N {
        for j in 0..<M {
            let data = edges[j]
            if dist[data.cur] != INF && dist[data.nxt] > dist[data.cur] + data.weight {
                dist[data.nxt] = dist[data.cur] + data.weight
                if i == N-1 {
                    return true
                }
            }
        }
    }
    return false
}
let isCycle = bellmanFord(1)
if isCycle {
    print("-1")
} else {
    for i in 2...N {
        if dist[i] == INF {
            print("-1")
        }
        else {
            print(dist[i])
        }
    }
}
    

