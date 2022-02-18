import Foundation

func solution(_ n:Int, _ results:[[Int]]) -> Int {
    var player_losers = Array(repeating: Set<Int>(), count: n + 1) // 이긴 선수들
    var player_winners = Array(repeating: Set<Int>(), count: n + 1) // 진 선수들
    
    for result in results {
        let winner = result[0], loser = result[1]
        
        player_losers[winner].insert(loser)
        player_winners[loser].insert(winner)
    }
    
    for player in 1...n {
        for loser in player_losers[player] { // player 한테 진 선수들은
            player_winners[player].forEach { player_winners[loser].update(with: $0) } //player 를 이긴 선수들도 다 이긴걸로 처리
        }
        
        for winner in player_winners[player] {// player 를 이긴 순수들은
            player_losers[player].forEach { player_losers[winner].update(with: $0) } //player 한테 진 사람들도 다 진걸로 처리
        }
    }
    
    var answer = 0
    
    for player in 1...n {
        if player_winners[player].count + player_losers[player].count == n - 1 {
            answer += 1
        }
    }
    return answer
}

