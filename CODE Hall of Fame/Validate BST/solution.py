# Cracking the Coding Interview
# pg 110. prob. 4.5
# *Thought the logic and approach for this code was very elegant

# Approach:
# BST: left.data <= root.data < right.data
# use Min and Max to keep track of the range
# in whether or not the BST condition above is met
# recurse through the tree while range gets narrower

# Time Complexity: O(n)
#  - n nodes in tree
# Space Complexity: O(log n)
#  - recurses through height of tree


def validate(root, minn, maxn):
    if not root:
        return True
    if minn and root.key < minn or maxn and root.key > maxn:
        return False
    if not validate(root.left, minn, root.key) or not validate(root.right, root.key, maxn):
        return False
    return True


def solution(root):
    return validate(root, None, None)
