"""
Runtime: 300 ms, faster than 15.25% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.3 MB, less than 16.95% of Python3 online submissions for Range Sum of BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, val = [root], 0
        
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)

                if low <= node.val <= high :
                    val += node.val
        
        return val
