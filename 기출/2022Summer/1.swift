import Foundation

func getMaskLifespan(_ normalDust: Int, _ microDust: Int) -> Int? {
    if normalDust < 81 && microDust < 36 { // 마스크 필요 X
        return nil
    } else if normalDust >= 151 && microDust >= 76 { // 매우 나쁨 마스크
        return 0
    } else { // 일반 마스크
        return 2
    }
}

func solution(_ atmos:[[Int]]) -> Int {
    var answer = 0
    var currentMaskLife = 0
    
    for data in atmos {
        let normalDust = data[0]
        let microDust = data[1]
        guard let maskLifespan = getMaskLifespan(normalDust, microDust) else {
            if currentMaskLife > 0 {
                currentMaskLife -= 1
            }
            continue
        }
        if maskLifespan == 0 { // 매우 나쁨 마스크
            if currentMaskLife == 0 {
                answer += 1
            }
            currentMaskLife = 0 // 바로 폐기
        }
        if maskLifespan == 2 { // 일반 마스크
            if currentMaskLife == 0 {
                answer += 1
                currentMaskLife = 2
            } else {
                currentMaskLife -= 1
            }
        }
    }
    return answer
}

let atmos = [[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]
solution(atmos)

