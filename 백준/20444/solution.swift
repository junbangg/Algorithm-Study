import Foundation
let nk = readLine()!.split(separator: " ").compactMap{Int($0)}
let N = nk[0]
let K = nk[1]

func binarySearch(_left: Int, _right: Int) -> Bool {
    var left = _left
    var right = _right

    while left < right {
        let mid = left + (right - left) / 2
        let cuts = (mid+1) * (N-mid+1)

        if (cuts == K) {
            return true 
        } else if(cuts < K) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return false
}

let answer = binarySearch(_left: 0, _right: N/2 + 1)
print(answer == true ? "YES" : "NO")