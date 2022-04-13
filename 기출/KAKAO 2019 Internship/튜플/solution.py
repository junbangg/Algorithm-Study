def getNumbers(string):
    data = []
    # 전처리
    isOpen = False
    number, buffer = [], []
    
    for c in string[1:-1]:
        if c == '{':
            isOpen = True
            continue
        if isOpen:
            if c.isdigit():
                number.append(c)
            elif c == ',':
                if number:
                    buffer.append(int(''.join(number)))
                number = []
            else: # }
                isOpen = False
                if number:
                    buffer.append(int(''.join(number)))
                    number = []
                data.append(buffer)
                buffer = []
    return data

def getTuple(numbers):
    _set = set()
    tuple = []
    for data in sorted(numbers, key = len):
        unique = set(data) - _set
        tuple.extend(list(unique))
        for num in list(unique):
            _set.add(num)
    return tuple

def solution(s):
    numbers = getNumbers(s)
    return getTuple(numbers)

tc1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
tc2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
tc3 = "{{20,111},{111}}"
print(solution(tc2))