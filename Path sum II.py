# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.res = []
    
    def findAllPathSum(self, root, sum_, cur_sum):
        if root == None or root == []:
            return []
        if root.left == None and root.right == None and sum_ == sum(cur_sum) + root.val:
            cur_sum.append(root.val)
            self.res.append(cur_sum)
            return
        left = self.findAllPathSum(root.left, sum_, cur_sum + [root.val])
        right = self.findAllPathSum(root.right, sum_, cur_sum + [root.val])
        
        
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.findAllPathSum(root, sum_, [])
        
        return self.res
        