def solution(msg):
    dic = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
        'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    answer = []
    lastNumber = 27
    currentIndex = 0
    while currentIndex < len(msg):
        currentString = msg[currentIndex]
        nextIndex = currentIndex + 1
        while nextIndex < len(msg) and currentString + msg[nextIndex] in dic:
            nextIndex += 1
        if currentIndex < nextIndex - 1:
            currentString = currentString + msg[nextIndex - 1]
        answer.append(dic[currentString])
        if nextIndex < len(msg):
            dic[currentString + msg[nextIndex]] = lastNumber
            lastNumber += 1
        currentIndex = nextIndex
    return answer
tc = 'KAKAO'
print(solution(tc))