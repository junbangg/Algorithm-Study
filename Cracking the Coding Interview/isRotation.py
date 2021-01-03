def isRotation(s1,s2):
    length = len(s1)
    if len(s2) == length and length > 0:
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
def isSubstring(s1,s2):
    if s1.count(s2) > 0:
        return True
    return False

#or

def isRotation2(s1,s2):
    if len(s1) != len(s2):
        return False
    s1 = s1 + s1
    if s2 not in s1: return False
    return True



