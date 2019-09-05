/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() {}

    Node(int _val, Node* _left, Node* _right, Node* _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* connect(Node* root) {
    
        Node *prev = NULL, *head = root;
        while( head != NULL)
        {
            Node *cur = head;
            prev = NULL;
            head = NULL;
            while(cur != NULL)
            {   if(cur->left != NULL)
                {
                    if(prev != NULL)
                        prev->next = cur->left; 
                    else
                        head = cur->left;       
                    prev = cur->left;    
                    
                }
                if(cur->right != NULL)
                {
                    if(prev != NULL)
                        prev->next = cur->right;
                    else
                        head = cur->right;
                    prev = cur->right;
                } 
                cur = cur->next;
            }
            
        }

        return root;
        
    }
};