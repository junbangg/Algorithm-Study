import Foundation

struct Fireball {
    var x: Int
    var y: Int
    let mass: Int
    let direction: Int
    let speed: Int

    var currentPosition: (Int, Int) {
        return (x, y)
    }

    func getNextPosition(boardLength: Int) -> (Int, Int) {
        // N, NE, E, SE, S, SW, W, NW
        let dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        let dy = [0, 1, 1, 1, 0, -1, -1, -1]

        var nx = (self.x + dx[self.direction] * self.speed) % boardLength
        var ny = (self.y + dy[self.direction] * self.speed) % boardLength

        nx = nx < 0 ? boardLength - 1 + nx : nx
        ny = ny < 0 ? boardLength - 1 + ny : ny
        
        return (nx % boardLength, ny % boardLength)
    }

    mutating func changePosition(x: Int, y: Int) {
        self.x = x
        self.y = y
    }
}

func multiplyFireballs(x: Int, y: Int, fireballs: [Fireball]) -> [Fireball]? {
    let originalLength = fireballs.count
    let newMass = fireballs.reduce(0) { partialResult, fireball in
        return partialResult + fireball.mass
    } / 5
    let newSpeed = fireballs.reduce(0) { partialResult, fireball in
        return partialResult + fireball.speed
    } / fireballs.count
    let isAllEven = fireballs.filter { $0.direction % 2 == 0 }
        .count == originalLength ? true : false
    let isAllOdd = fireballs.filter { $0.direction % 2 != 0 }
        .count == originalLength ? true : false
    let newDirections = isAllOdd || isAllEven ? [0, 2, 4, 6] : [1, 3, 5, 7]

    
    if newMass == 0 {
        return nil
    }
    
    var newFireballs: [Fireball] = []
    
    for i in 0..<4 {
        let newFireball = Fireball(
            x: x,
            y: y,
            mass: newMass,
            direction: newDirections[i],
            speed: newSpeed
        )
        newFireballs.append(newFireball)
    }
    
    return newFireballs
}

func simulate(_ board: inout [[[Fireball]]], _ fireballs: [Fireball]) -> [Fireball] {
    let boardLength = board.count
    //move
    for fireball in fireballs {
        var fireball = fireball
        let (x, y) = fireball.currentPosition
        let (nx, ny) = fireball.getNextPosition(boardLength: boardLength)

        board[x][y].removeLast() // checkout
        fireball.changePosition(x: nx, y: ny)
        board[nx][ny].append(fireball)
    }
    print("moved!")
    printBoard(board)
    var newFireballs: [Fireball] = []
    // apply fireball
    for x in 0..<boardLength {
        for y in 0..<boardLength {
            if board[x][y].count > 1 {
                guard let multipliedFireballs = multiplyFireballs(x: x, y: y, fireballs: board[x][y]) else {
                    board[x][y] = []
                    continue
                }
                board[x][y] = multipliedFireballs
                newFireballs.append(contentsOf: multipliedFireballs)
            } else if board[x][y].count == 1 {
                newFireballs.append(contentsOf: board[x][y])
            }
        }
    }
    return newFireballs
}

func getFireballMassTotal(of board: [[[Fireball]]]) -> Int {
    var massTotal = 0

    for x in 0..<N {
        for y in 0..<N {
            if board[x][y].isEmpty {
                continue
            }
            massTotal += board[x][y].reduce(0) { partialResult, fireball in
                return partialResult + fireball.mass
            }
        }
    }
    return massTotal
}

func printBoard(_ board: [[[Fireball]]]) {
    for i in 0..<board.count {
        print(board[i])
    }
}

let NMK = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NMK[0]
let M = NMK[1]
let K = NMK[2]

var board: [[[Fireball]]] = Array(repeating: Array(repeating: [], count: N), count: N)
var fireballs: [Fireball] = []

for _ in 0..<M {
    let data = readLine()!.split(separator: " ").compactMap { Int($0) }
    let x = data[0]-1
    let y = data[1]-1
    let mass = data[2]
    let speed = data[3]
    let direction = data[4]

    let fireball = Fireball(
        x: x,
        y: y,
        mass: mass,
        direction: direction,
        speed: speed
    )
    fireballs.append(fireball)

    board[x][y].append(fireball)
}


for i in 0..<K {
    print(i)
    print("Before")
    print(fireballs)
    printBoard(board)
    fireballs = simulate(&board, fireballs)
    print("After ")
    print(fireballs)
    printBoard(board)
}


print(getFireballMassTotal(of: board))
//count

// tc
// 4 2 1
// 1 1 5 2 2
// 1 4 7 5 6

// 4 2 1
// 1 1 5 2 2
// 1 4 7 0 6

// 4 2 1
// 1 1 5 2 2
// 1 4 7 4 6
