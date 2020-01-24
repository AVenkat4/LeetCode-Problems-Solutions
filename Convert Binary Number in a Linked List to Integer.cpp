/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    long long int sum = 0, ind = 1;
    
    void recur(ListNode *root)
    {
        if(root == NULL)
        {
            ind = 1;
            return;
        }
        recur(root->next);
        if(root->val == 1)
            sum += ind;
        ind = ind << 1;
    }
    
    int getDecimalValue(ListNode* head) {
        
        ListNode *p = head;
        recur(p);
        
        return sum;
    }
};