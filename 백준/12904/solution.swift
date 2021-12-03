var S = readLine()!.compactMap { String($0) }
var T = readLine()!.compactMap { String($0) }

while S.count != T.count {
    if T.last == "A" {
        T.removeLast()
    } else {
        T.removeLast()
        T = T.reversed()
    }
}
var answer = 0
if T == S {
    answer = 1
}
print(answer)