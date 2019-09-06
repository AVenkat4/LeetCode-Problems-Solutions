/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* BTree(vector<int>& inorder, int begi, int endi, vector<int>& postorder, unordered_map<int, int>& m)
    {
        if((endi - begi) < 0)
            return NULL;
        
        int rootval = postorder.back();
        TreeNode *root = new TreeNode(rootval);
        
        postorder.pop_back();
        int split = m[rootval];
        root->right = BTree(inorder, split+1, endi, postorder, m);
        root->left = BTree(inorder, begi, split-1, postorder, m);
        
        
        return root;
        
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        
        unordered_map<int, int> m;
        int n = inorder.size();
        for(int i = 0; i < n; i++)
            m[inorder[i]] = i;
        
        TreeNode *root = BTree(inorder, 0, n-1, postorder, m);
        
        return root;
    }
};