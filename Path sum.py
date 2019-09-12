# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def checkHasPathSum(self, root, sum, cur_sum):
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            return cur_sum + root.val == sum
        
        return self.checkHasPathSum(root.left, sum, cur_sum + root.val) or self.checkHasPathSum(root.right, sum, cur_sum + root.val)
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.checkHasPathSum(root, sum, 0)
        
        
        