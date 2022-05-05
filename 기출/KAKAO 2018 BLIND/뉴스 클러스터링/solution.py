from collections import Counter

# ->  [intersectionSize, unionSize]
def getIntersectionAndUnionSize(set1, set2):
    # get counts
    set1Counter = Counter(set1)
    set2Counter = Counter(set2)

    # convert to actual set
    set1 = set(set1)
    set2 = set(set2)

    # get intersection
    intersection = set1 & set2
    
    # get jaccard intersection
    intersectionStrings, unionStrings = [], []

    for string in intersection:
        minCount = min(set1Counter[string], set2Counter[string])
        intersectionStrings.extend([string] * minCount)
        
    # get union intersection
    union = set1 | set2
    for string in union:
        maxCount = max(set1Counter[string], set2Counter[string])
        unionStrings.extend([string] * maxCount)
        
    return len(intersectionStrings), len(unionStrings)

def getJaccard(set1, set2):
    if not set1 and not set2:
        return 1

    intersectionSize, unionSize = getIntersectionAndUnionSize(set1, set2)
    #TODO precision check
    return intersectionSize / unionSize

def convertToSet(string):
    output = []
    # split by 2
    for i in range(1, len(string)):
        temp = string[i-1:i+1].strip()
        if temp.isalpha() and len(temp) == 2:
            output.append(temp.upper())
    return output


def convertToAnswerFormat(number):
    return int(number * 65536)

def solution(str1, str2):
    set1 = convertToSet(str1)
    set2 = convertToSet(str2)
    number = getJaccard(set1, set2)
    answer = convertToAnswerFormat(number)
    return answer

# set1 = ['A', 'A', 'B', 'B', 'C']
# set2 = ['A', 'B', 'B', 'D', 'E']
# print(getJaccard(set1, set2))
# set1 = ['FR', 'RA', 'AN', 'NC', 'CE']
# set2 = ['FR', 'RE', 'EN', 'NC', 'CH']
# answer = 0.25
# if answer == getJaccard(set1, set2):
#     print("True")
# else:
#     print("False")

tc1 = 'A CD '
tc2 = 'A CD E'
tc3 = 'ABCDEFG'
tc4 = 'france'
tc5 = 'french'
print(convertToSet(tc5))

test = 'ab++'
result = test.isalpha()
if result:
    print("raerlkj")
else:
    print("nononon")