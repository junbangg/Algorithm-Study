
let N = Int(readLine()!)!

var houses: [(Int, Int)] = []
var totalPeople = 0

for _ in 0..<N {
    let indexPeople = readLine()!.split(separator: " ").compactMap { Int($0) }
    let index = indexPeople[0]
    let people = indexPeople[1]

    totalPeople += people
    houses.append((index, people))
}

houses.sort {
    $0.0 < $1.0
}

var peopleCount = 0

for (index, people) in houses {
    peopleCount += people

    if peopleCount > totalPeople / 2 {
        print(index)
        break
    }
}

