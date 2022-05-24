import Foundation

struct Point {
    let x: Int
    let id: Int
    let side: String
}

func solution(_ points: [Point]) {
    var stack: [Point] = []

    for point in points {
        if !stack.isEmpty {
            if stack.last!.id == point.id {
                stack.removeLast()
                continue
            } else if stack.last!.side != point.side {
                print("NO")
                exit(0)
            }
        }
        stack.append(point)
    }

    print("YES")
}

let N = Int(readLine()!)!
var points: [Point] = []

for i in 0..<N {
    let XR = readLine()!.split(separator: " ").compactMap { Int($0) }

    points.append(Point(x: XR[0] - XR[1], id: i, side: "L"))
    points.append(Point(x: XR[0] + XR[1], id: i, side: "R"))
}
points.sort(by: {
    $0.x < $1.x
})

solution(points)