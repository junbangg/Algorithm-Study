public func solution(_ A : inout [Int]) -> Int {
    if A == [] {
        return 0
    }
    var minPrice = Int.max
    var profit = 0
    for price in A {
        minPrice = min(price, minPrice)
        profit = max(profit, price - minPrice)
    }
    return profit
}
