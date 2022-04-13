from itertools import permutations

def isValidID(candidate_id, banned_id):
    for i in range(len(candidate_id)):
        if banned_id[i] == '*':
            continue
        if candidate_id[i] != banned_id[i]:
            return False
    return True

def isValidCandidate(candidates, banned):
    for i in range(len(candidates)):
        candidate_id, banned_id = candidates[i], banned[i]
        if len(banned_id) != len(candidate_id):
            return False
        if not isValidID(candidate_id, banned_id):
            return False
    return True

def solution(user_id, banned_id):
    candidates = permutations(user_id, len(banned_id))
    banned = set()

    for cand in candidates:
        if isValidCandidate(cand, banned_id):
            banned.add(''.join(sorted(list(cand))))

    return len(banned)