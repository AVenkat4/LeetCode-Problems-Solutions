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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode *result = new ListNode(0);
        ListNode *p3 = result;
        ListNode *p1 = l1, *p2 = l2;
        int sum = 0, carry = 0;
        while(p1 != NULL && p2!= NULL)
        {
            sum = p1->val + p2->val + carry;
            if(sum > 9)
            {    carry = 1;
                 sum = sum%10;
            }
            else
                carry = 0;
            ListNode *node = new ListNode(0);
            if(p3 != NULL)
                p3->next = node;
            p3 = node;
            p3->val = sum;
            p1 = p1->next;
            p2 = p2->next;
        }
        while(p1 != NULL)
        {
            sum = p1->val + carry;
            if(sum > 9)
            {
                carry = 1;
                sum = sum%10;
            }
            else
                carry = 0;
            ListNode *node = new ListNode(0);
            if(p3 != NULL)
                p3->next = node;
            p3 = node;
            p3->val = sum;
            p1 = p1->next;
            
        }
        while(p2 != NULL)
        {
            sum = p2->val + carry;
            if(sum > 9)
            {
                carry = 1;
                sum = sum%10;
            }
            else
                carry = 0;
            ListNode *node = new ListNode(0);
            if(p3 != NULL)
                p3->next = node;
            p3 = node;
            p3->val = sum;
            p2 = p2->next;
            
        }
        if(carry != 0)
        {
            ListNode *node = new ListNode(0);
            if(p3 != NULL)
                p3->next = node;
            p3 = node;
            p3->val = carry;
        }
        return result->next;
    }
};