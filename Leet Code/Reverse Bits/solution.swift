class Solution {
    func reverseBits(_ n: Int) -> Int {
        var bits : [Int] = []
        var n = n
        for i in 0...31 {
            bits.append(n & 1)
            n = n >> 1
        }
        bits.reverse()
        var answer = 0
        for i in 0...31 {
            answer = answer << 1
            answer += bits.popLast()!
        }
        return answer
    }
}
