class Solution:
    answer = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        answer = 0
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            self.answer = max(self.answer, left+right+2)
            return max(left, right) + 1
        dfs(root)
        return self.answer
