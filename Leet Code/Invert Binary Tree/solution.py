class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)
        invert(root)
        return root 
