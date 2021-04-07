public func solution(_ A : inout [Int]) -> Int {
    if A == [] {
        return 1
    }
    A.sort()
    for i in 0...A.count - 1 {
        if i+1 != A[i] {
            return i + 1
        }
    }
    return A.last! + 1
}
