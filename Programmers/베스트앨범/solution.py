from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i in range(len(genres)):
        genre_total[genres[i]] += plays[i]
        genre_songs[genres[i]].append((plays[i], i))
        
    for genre in genre_songs.keys():
        genre_songs[genre].sort(key=lambda x: (-x[0], x[1]))
    
    answer = []
    for genre, _ in sorted(genre_total.items(), key=lambda x: -x[1]):
        for i in range(2):
            songs = genre_songs[genre]
            if i < len(songs):
                answer.append(songs[i][1])
    
    return answer
