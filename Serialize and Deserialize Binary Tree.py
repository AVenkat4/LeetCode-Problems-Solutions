# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def doit(root):
            if root is not None:
                vals.append(str(root.val))
                doit(root.left)
                doit(root.right)
            else:
                vals.append("#")
        doit(root)
        #print(vals)
        return ' '.join(vals)
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(" ")
        def doit(ind):
            if vals[ind[0]] != "#":
                root = TreeNode(vals[ind[0]])
                ind[0] += 1
                root.left = doit(ind)
                ind[0] += 1
                root.right = doit(ind)
            else:
                root = None
            return root
        
        ind = [0]
        root = doit(ind)
        return root
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))