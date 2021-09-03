"""
Runtime: 30 ms, faster than 65.04% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 14.4 MB, less than 31.62% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val: int = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # BST이므로 오른쪽 자식 + 부모 + 왼쪽 자식  -> DFS 탐색 중위순회
        
        if root is None:
            return
        
        self.bstToGst(root.right)
        self.val += root.val
        root.val = self.val
        self.bstToGst(root.left)
        
        return root
