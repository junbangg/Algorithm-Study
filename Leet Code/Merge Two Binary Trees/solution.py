class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def merge(one, two):
            if one and two:
                newNode = TreeNode(one.val+two.val)
                newNode.left = merge(one.left, two.left)
                newNode.right = merge(one.right, two.right)
                return newNode
            else:
                return one or two
        return merge(root1, root2) 
