# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def FindMaxPathSum(self, root, res):
        if root == None:
            return 0
        left = self.FindMaxPathSum(root.left, res)
        right = self.FindMaxPathSum(root.right, res)
        left = 0 if left < 0 else left
        right = 0 if right < 0 else right
        #max_single = max(max(left, right) + root.val, root.val)
        
        #max_top = max(left + right + root.val, max_single)
        res[0] = max(left + right + root.val, res[0])
        #res[0] = max(res[0], max_top)
        
        return max(left, right) + root.val
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [float('-inf')]
        self.FindMaxPathSum(root, res)
        
        return res[0]