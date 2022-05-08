def getScore(compoundType, selection): # return (type, score)
    scores = [0, 3, 2, 1, 0, 1, 2, 3]
    type = compoundType[0] if selection < 4 else compoundType[1]

    return type, scores[selection]

def getSortedType(type):
    return ''.join(sorted(type))

def solution(survey, choices):
    # 하드코딩된 map{map}
    typeMap = {
        'RT': {'R': 0, 'T': 0},
        'CF': {'C': 0, 'F': 0},
        'JM': {'J': 0, 'M': 0},
        'AN': {'A': 0, 'N': 0}
    }
    # apply scores
    for index in range(len(survey)):
        type = survey[index]
        selection = choices[index]
        subType, score = getScore(type, selection)

        sortedType = getSortedType(type)

        typeMap[sortedType][subType] += score
    # 결과 산출
    answer = ''
    types = ['RT', 'CF', 'JM', 'AN']
    for type in types:
        scores = typeMap[type]
        answer += max(scores, key=scores.get)
    return answer

# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
print(solution(survey, choices))