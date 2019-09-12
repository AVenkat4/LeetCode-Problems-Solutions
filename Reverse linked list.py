# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return head
        
        p = head
        while p.next is not None:
            p = p.next
        
        cur_head = head
        head2 = head
        while cur_head != p:
            q = cur_head.next
            cur_head.next = p.next
            p.next = cur_head
            cur_head = q
            
        
        return cur_head