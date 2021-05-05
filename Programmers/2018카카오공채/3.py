def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cities = [city.lower() for city in cities]
    main = []
    answer = 0
    for city in cities:
        if city not in main:
            if len(main) == cacheSize:
                main.remove(main[0])
                main.append(city)
            else:
                main.append(city)
            answer += 5
        else:
            main.remove(city)
            main.append(city)
            answer += 1
    return answer

c = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(c, cities))
