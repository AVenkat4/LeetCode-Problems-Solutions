# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self, ):
        self.num = 0
        self.total = 0
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.total += 1

        if head.next == None:
            self.num += 1
            return
        self.removeNthFromEnd(head.next, n)
        if self.num == n:
            head.next = head.next.next
        self.num += 1
        if self.num == n and self.num == self.total:
            return head.next
        return head