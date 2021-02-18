def solution(name):
    answer = sum(ord(c) - 65 if c <= 'N' else 91 - ord(c) for c in name)
    idx = [i for i, j in enumerate(name) if j != 'A']
    cur = 0
    lname = len(name)
    while idx:
        first = min(abs(idx[0]-cur), lname - abs(idx[0] - cur))
        last = min(abs(idx[-1] - cur), lname - abs(idx[-1] - cur))
        if first <= last:
            answer += first
            cur = idx.pop(0)
        else:
            answer += last
            cur = idx.pop()
    return answer
