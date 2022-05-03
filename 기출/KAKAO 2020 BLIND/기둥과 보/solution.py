
# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

def isNotValid(result):
    for x, y, a in result:
        if a: # 기둥일 때
            if (x, y-1, 0) not in result and (x+1, y-1, 0) not in result and \
        not ((x-1, y, 1) in result and (x+1, y, 1) in result):
                return True
        else: # 보일 때
            if y != 0 and (x, y-1, 0) not in result and \
        (x-1, y, 1) not in result and (x, y, 1) not in result:
                return True
    return False

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b: # create
            answer.append(item)
            if isNotValid(answer):
                answer.remove(item)
        elif item in answer: # delete
            answer.remove(item)
            if isNotValid(answer):
                answer.append(item)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))