import Foundation
// O(n^2)
func solution(_ needs:[[Int]], _ r:Int) -> Int {
    // create dictionary -> counts(sorted)
    let robots : [Int] = Array(0...needs[0].count-1)
    let mappedItems = robots.map { ($0, 0) }
    var counts = Dictionary(mappedItems, uniquingKeysWith: +)
    for row in needs {
        for i in 0...row.count-1 {
            if row[i] == 1 {
                counts[i]! += 1
            }
        }
    }
    let sortedCounts = counts.sorted {
        return $0.value > $1.value
    }
    // extract target indexes (candidates for optimized solution)
    var targets = [Int]()
    for i in 0...r-1 {
        targets.append(sortedCounts[i].key)
    }
    // search for target indexes in needs
    // flag used to check if components are valid targets
	var answer = 0
    for row in needs {
        var flag = false
        for i in 0...row.count-1 {
            if row[i] == 1 {
                if targets.contains(i) {
                    flag = true
                } else {
                    flag = false
                }
            } 
        }
        if flag {
            answer += 1
        }
    }
    return answer
}
