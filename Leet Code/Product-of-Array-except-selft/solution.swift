import UIKit

// [-1, 0, 2, 3, 4, -1, 0] -> []
// 리턴 값
// 모든 i 에 대허서 i 번쨰 원소를 제외한 나머지 원소를 곱한 값을 리턴

// [-1, 0, 2, 3, 4, -1, 0]
//-> [0, 0, 0, 0, 0, 0, 0]

// [-1, 1, 0, -3, 3]

// [-1, 0, 2, 3, 4, -1, 0]
// total = 24
//
// isZero = true
// isSingleZero = true
//
//
//
//[0, 0, 9, 0, 0]
//
//[-1, 1]
//
//[1, -1]

func solution(_ numbers: [Int]) -> [Int] {
    var answer: [Int] = Array(repeating: 0, count: numbers.count)
    var total = 1
    var zeroCount = 0
    
    for number in numbers {
        if number == 0 {
            zeroCount += 1
        } else {
            total *= number
        }
    }
    
    for (index, number) in numbers.enumerated() {
        var inputNumber = 0

        if zeroCount == 0 {
            inputNumber = total / number
        } else if zeroCount == 1 && number == 0 {
            inputNumber = total
        }
        answer[index] = inputNumber
    }

    return answer
}

let tc1 = [-1, 0, 2, 3, 4, -1, 0]
let tc2 = [-1, 1, 0, -3, 3]
let tc3 = [-1, 1]

solution(tc3)

