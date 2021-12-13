import Foundation
/// 1


/// 2

///3
public func solution(_ M : Int, _ N : Int) -> Int {
    let x = Int(sqrt(Double((4 * N) + M)))
    var answer = 0
    if x % 2 == 0 {
        answer = x
    } else {
        let maximumNSquares = (x-1) * (x-1) / 4
        let usableNSquares = min(maximumNSquares, N)
        if 4 * usableNSquares + M < x * x {
            answer = x - 1
        } else {
            answer = x
        }
    }
    return answer
}

solution(13, 3)


