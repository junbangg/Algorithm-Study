// Swift Solution
import Foundation

func solution(_ land:[[Int]]) -> Int{
    var tland = land
    let length = tland.count - 1
    for i in 1...tland.count - 1 {
        tland[i][0] += Array(arrayLiteral: tland[i-1][1], tland[i-1][2], tland[i-1][3]).max()!
        tland[i][1] += Array(arrayLiteral: tland[i-1][0], tland[i-1][2], tland[i-1][3]).max()!
    		tland[i][2] += Array(arrayLiteral: tland[i-1][0], tland[i-1][1], tland[i-1][3]).max()!
        tland[i][3] += Array(arrayLiteral: tland[i-1][0], tland[i-1][1], tland[i-1][2]).max()!
    }
    return tland[length].max()!
}
