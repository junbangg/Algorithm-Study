import UIKit

// 화면상의 두개의 직사각형
// 포함
// or
// 겹쳐져있는지




struct Point {
    let x: Int
    let y: Int
}

// p1: 0,0 , p2: 0, 10, p3: 10, 10, p4: 10, 0
struct Rectangle {
    let p1, p2, p3, p4: Point
    
    func isIntersected(with other: Rectangle) -> Bool {
        
    }
    
    func isContaining(_ other: Rectangle) -> Bool {
        if self.p1.x <= other.p1.x && 
    }
}

// 포함
let a = Rectangle(p1: Point(coordinates: Coordinate(x: 0, y: 0)), p2: Coordinate(x: 0, y: 10), p3: Coordinate(x: 10, y: 0), p4: Coordinate(x: 10, y: 10))

let b = Rectangle(p1: Point(coordinates: Coordinate(x: 1, y: 1)), p2: Point(coordinates: Coordinate(x: 1, y: 9)), p3: Point(coordinates: Coordinate(x: 9, y: 1)), p4: Point(coordinates: Coordinate(x: 9, y: 9)))

//겹침
let a = Rectangle(p1: Point(coordinates: Coordinate(x: 0, y: 0)), p2: Coordinate(x: 0, y: 10), p3: Coordinate(x: 10, y: 0), p4: Coordinate(x: 10, y: 10))

let b = Rectangle(p1: Point(coordinates: Coordinate(x: 2, y: 2)), p2: Coordinate(x: 2, y: 10), p3: Coordinate(x: 2, y: 10), p4: Coordinate(x: 12, y: 12))


