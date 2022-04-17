def getTuple(numbers):
    _set = set()
    tuple = []
    for data in sorted(numbers, key = len):
        unique = set(data) - _set
        tuple.extend(list(unique))
        for num in list(unique): _set.add(num)
    return tuple

def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    numbers = map(lambda x: x.split(","), s)
    
    return getTuple(numbers)