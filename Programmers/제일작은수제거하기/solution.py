def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]

#or
def solution(arr):
    return [i for i in arr if i>min(arr)] or [-1]
