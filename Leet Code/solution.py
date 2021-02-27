class Solution:
    def isValid(self, s: str) -> bool:
        dic = { ")" : "(",
               "]" : "[",
               "}" : "{" }
        stack = []
        #edge case
        if not s or len(s) % 2 != 0:
            return False
        for p in s:
            if p in dic.values():
                stack.append(p)
            elif not stack:
                return False
            else:
                if stack.pop() != dic[p]:
                    return False
        if not stack:
            return True

# or
class Solution:
    def isValid(self, s: str) -> bool:
        dic = { ")" : "(",
               "]" : "[",
               "}" : "{" }
        stack = []
        #edge case
        if not s or len(s) % 2 != 0:
            return False
        for p in s:
            if p not in dic:
                stack.append(p)
            elif not stack or stack.pop() != dic[p]:
                return False
        return len(stack) == 0
