class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
        let depth = (matrix.count + 1) / 2
        var answer: [Int] = []
        let rowMax = matrix.count
        let colMax = matrix[0].count
        let maxNumberCount = rowMax * colMax
        
        for d in 0..<depth {
            // Right
            for j in d..<colMax-d-1 {
                let x = d
                let y = j
                answer.append(matrix[x][y])
                if answer.count == maxNumberCount {
                    break
                }
            }
            // Down
            for i in d..<rowMax-d-1 {
                let x = i
                let y = colMax-d-1
                answer.append(matrix[x][y])
                if answer.count == maxNumberCount {
                    break
                }
            }
            // Left
            for j in stride(from: colMax-d-1, to: d, by: -1) {
                let x = rowMax-d-1
                let y = j
                answer.append(matrix[x][y])
                if answer.count == maxNumberCount {
                    break
                }
            }
            // Up
            for i in stride(from: rowMax-d-1, to: d, by: -1) {
                let x = i
                let y = d
                answer.append(matrix[x][y])
                if answer.count == maxNumberCount {
                    break
                }
            }
            if answer.count == maxNumberCount {
                break
            }
        }
        if answer.count == maxNumberCount-1 {
            answer.append(matrix[rowMax/2][colMax/2])
        }
        return answer
    }
}
