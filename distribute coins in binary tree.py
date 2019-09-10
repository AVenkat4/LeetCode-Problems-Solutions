# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def postOrder(self, root, moves):
        
        if root == None:
            return 0
        left = self.postOrder(root.left, moves)
        right = self.postOrder(root.right, moves)
        moves[0] += abs(left) + abs(right)
        return root.val + left + right - 1
        
    
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        moves = [0]
        self.postOrder(root, moves)
        
        return moves[0]
        