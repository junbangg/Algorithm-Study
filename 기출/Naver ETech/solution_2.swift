func solution(_ S: String, _ A : [Int]) -> String {
    var dic = Dictionary<Int, String>()
    var answer = ""
    for (i, v) in S.enumerated() {
        dic[i] = String(v)
    }
    var next = 0
    repeat {
        //Send
        let send = dic[next]!
        // Empty original letters
        dic[next]! = ""
        // Receive
        answer = send + dic[A[next]]!
        dic[A[next]]! = answer
        next = A[next]
    } while next != 0
    return answer
}

var S = "cdeenetpi"
var A = [5,2,0,1,6,4,8,3,7]
solution(S, A)


