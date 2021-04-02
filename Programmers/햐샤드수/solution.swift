func solution(_ x:Int) -> Bool {
    let x_str = Array(String(x))
    var sum = 0
    for c in x_str {
        sum += c.wholeNumberValue ?? 0
    }
    return x % sum == 0
}
