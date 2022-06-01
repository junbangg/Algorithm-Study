import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    typealias Song = (plays: Int, id: Int)
    var genre_total: [String: Int] = [:]
    var genre_songs: [String: [Song]] = [:]
    // 해시 setup
    for i in 0..<genres.count {
        let genre = genres[i]
        let plays = plays[i]

        genre_total[genre, default: 0] += plays
        genre_songs[genre, default: []].append(Song(plays: plays, id: i))
    }
    // 장르별 노래 정렬 
    for (genre, songs) in genre_songs {
        let songs = songs.sorted(by: {
            if $0.plays == $1.plays {
                return $0.id < $1.id
            }
            return $0.plays > $1.plays
        })
        genre_songs[genre, default: []] = songs
    }
    // 장르 정렬
    let orderedGenres = genre_total
        .map { ($0.0, $0.1) }
        .sorted(by: {
            $0.1 > $1.1
        })
        .map { $0.0 }
    
    var answer: [Int] = []
    
    // 각 장르별 2곡 정답에 추가
    orderedGenres
        .forEach {
            for i in 0..<2 {
                let songs = genre_songs[$0, default: []]
            
                if i < songs.count {
                    answer.append(songs[i].id)
                }
            }
        }
    
    return answer
}
