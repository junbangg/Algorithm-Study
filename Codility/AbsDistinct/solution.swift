public func solution(_ A : inout [Int]) -> Int {
    for (i, v) in A.enumerated() {
        A[i] = abs(v)
    }
    return Set(A).count
}
