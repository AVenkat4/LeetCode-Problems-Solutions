# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self,):
        self.count = 0
        
    def DFS(self, root, sum, cur_sum):
        if root == None:
            return 0
        
        if cur_sum + root.val == sum:
            self.count += 1
        
        return (1 if cur_sum + root.val == sum else 0) + self.DFS(root.left, sum, cur_sum + root.val) + self.DFS(root.right, sum, cur_sum + root.val)
    
    
    def numPathSum(self, root, sum):
        if root == None:
            return 0
        return self.DFS(root, sum, 0) + self.numPathSum(root.left, sum) + self.numPathSum(root.right, sum)
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        self.numPathSum(root, sum)
        
        return self.count
        

		