public func solution(_ A : inout [Int], _ K : Int) -> [Int] {
    // write your code in Swift 4.2.1 (Linux)
    if A == [] {
         return A
    }
    var k = K
    while k > 0 {
        A.insert(A.removeLast(), at: 0)
        k -= 1
    }
    return A
}
