import Foundation

func solution(_ stepCounts:[Int]) -> Int {
    //if bonus == 10000 counter ++
    // if counter == 1, 3, 5 add 10000
    // if day % 7 == 0: bonus = 0 and counter = 0
    var total: Int = 0
    var counter: Int = 0
    for day in 0..<stepCounts.count {
        if day % 7 == 0 {
            counter = 0
        }
        if stepCounts[day] >= 10000 {
            counter += 1
            if counter == 1 || counter == 3 || counter == 5 {
                total += 10000
            }
        }
        if stepCounts[day] > 10000 {
            total += 10000
        } else {
            total += stepCounts[day]
        }
        
    }
    return total
}
//
let testCases: [[Int]] = [[5000], [10000, 0, 10000], [10000, 5000, 10000, 1000, 15000], [2312, 13929, 1528, 11877, 2486, 6042, 13233, 6414], [9198, 3472, 5439, 6174, 10202]]
let answers: [Int] = [5000, 30000, 56000, 68782, 44283]
for i in 0 ..< testCases.count {
    let answer = solution(testCases[i])
    if answer == answers[i] {
        print("Correct! (Result: \(answer), Answer: \(answers[i]))")
    } else {print("Incorrect! (Result: \(answer), Answer: \(answers[i]))")}
}
