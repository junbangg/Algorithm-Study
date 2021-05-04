import collections
def solution(user_id, banned_id):
    answer = set()
    length = len(banned_id)

    def check(user, banned):
        if len(user) != len(banned):
            return False
        for i, v in enumerate(banned):
            if v != '*' and user[i] != banned[i]:
                return False
        return True

    def dfs(path, user_id, banned_id):
        if len(path) == length:
            answer.add(tuple(path))
            return
        for key in dic:
            nextPath = []




    # narrow down candidates
    cand_user = set()
    dic = collections.defaultdict(list)
    for id in user_id:
        for ban in banned_id:
            if check(id, ban):
                dic[ban].append(id)

    dfs([], list(cand_user), banned_id)
    answer = [sorted(list(a)) for a in list(answer)]
    answer = set(map(tuple, answer))
    return len(answer)

def solution(user_id, banned_id):
    answer = set()
    length = len(banned_id)

    def check(user, banned):
        if len(user) != len(banned):
            return False
        for i, v in enumerate(banned):
            if v != '*' and user[i] != banned[i]:
                return False
        return True

    def dfs(path, user_id, banned_id):
        if len(path) == length:
            answer.add(tuple(sorted(path)))
            return
        for index, id in enumerate(user_id):
            for i, ban in enumerate(banned_id):
                if check(id, ban):
                    next_ids = user_id[:]
                    next_ids.pop(index)
                    next_banned = banned_id[:]
                    next_banned.pop(i)
                    dfs(path+[id], next_ids, next_banned)
    # narrow down candidates
    cand_user = set()
    for id in user_id:
        for ban in banned_id:
            if check(id, ban):
                cand_user.append(id)

    dfs([], list(cand_user), banned_id)
    return len(answer)
#user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
#user_id = ["frodo", "fradi", "abc123"]
#banned_id = ["fr*d*", "abc1**"]
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
dfs([], user_id, banned_id)
print(answer)

