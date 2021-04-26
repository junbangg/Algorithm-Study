func solution(n lastNode: Int, edges: [(Int, Int)]) -> Int { 
    var edgeData = [Int: Array<Int>]() 
    // edge 정보를 setup 
    for edge in edges { 
        if var array = edgeData[edge.0] { 
        array.append(edge.1) 
        edgeData[edge.0] = array 
        } else { 
            edgeData[edge.0] = [edge.1] 
        } 
    } 
    // 1. 궁극적으로 원하는 값 (재귀를 돌며 수집할 값) 
    var result = 0 

    func dfs(node: Int, visited: [Int]) { 
        guard node != lastNode else { 
        // 2. 재귀를 멈추는 조건 
            result += 1 
            return 
        } 
        guard let neighbors = edgeData[node] else { return } 
        for edge in neighbors { 
        // 현재의 노드에서 이동할 수 있는 노드 중, 아직 방문하지 않은 곳으로 가본다 (중복 방지) 
            guard visited.contains(edge) == false else { continue } 
            dfs(node: edge, visited: visited + [edge]) 
        } 
    } 
    // 3. 초기값으로 어떤 것을 넘길지 
    dfs(node: 1, visited: [1]) 
    return result
} 
solution(n: 5, edges: [(1, 2), (1, 3), (1, 4), (2, 1), (2, 4), (2, 5), (3, 2), (3, 4), (4, 5)])

