/// 스트라이크 & 볼 계산 함수
// [1, 3, 4]
// [5, 2, 1]

// 1. 교집합 생성해서 안에 들어있는 숫자의 개수를 ball 로 설정 - > 최대 3개가 나올 수 있음
// 2. 두개의 collection에 있는 숫자들에 대해 index 로 하나씩 비교..
//     - 만약에 스트라이크가 발생하면, strike++, ball--


/// Error 를 사용할지말지


/// set 는 array 처럼 index 로 접근 불가... set의 숫자를 배열로 옮겨 담아야할지도
// let set1: Set<Int> = [1,2,3]
// let set2: Set<Int> = [1,2,6]

// var balls = set1.intersection(set2).count
// var strikes = 0
// print(set1[2])
// for i in 0..<3 {
//     if set1[i] == set2[i] {
//         strikes += 1
//         balls -= 1
//     }
// }

// print("Strike: \(strikes), Balls: \(balls)")



2. 다음 함수를 구현합니다
    i. 1~9 사이의 세 개의 임의의 정수를 생성하여 반환하는 함수(생성한 세 개의 정수는 중복된 수가 없어야합니다)

- 1~9 사이의 난수 생성
- 중복된 수가 있는지 확인
- 반환


중복되지않은 숫자 3개가 들어있는 set 가 만들어질때까지
set <- 난수를 넣자


set() <- 난수 집어넣는다 3

set(3)

set(3) <- 난수 넣는다 3

set(3, 2, 5) 




세 개의 정수를 전달받아 [1-1]의 수와 비교하여 볼과 스트라이크 결과를 반환하는 함수


[2, 5, 7]
[7, 2, 5]

num1 && num2 = [2, 5, 7]

//교집합 원소의 개수
var ball = [2, 5, 7].count (3)

strike = 0
for i in 0..<3 {
    // strike 조건
    if num1[i] == num2[i] {
        strike += 1
        ball -= 1
    }
}

strike = 0
// 볼
ball = 3