"""
Runtime: 113 ms, faster than 9.89% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.7 MB, less than 59.52% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums)//2 
        
        node = TreeNode(val = nums[mid],
                        left = self.asortedArrayToBST(nums[:mid]),
                        right = self.sortedArrayToBST(nums[mid+1:])
                       )
        
        return node
