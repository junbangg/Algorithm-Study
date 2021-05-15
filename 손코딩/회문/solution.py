# Palindrome

# baaxaab -> odd number
# baaxxaab -> even number
def checkPalindrome(s):
    left, right = 0, len(s) - 1
    while s[left] == s[right] and left <= right:
        left += 1
        right -= 1
        if left > right:
            return True
    return False

a = 'baaxaab'
b = 'baaxxaab'
print(checkPalindrome(a))



