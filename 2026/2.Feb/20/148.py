# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        listNum = []
        curr = head
        while curr != None:
            listNum.append(curr.val)
            curr = curr.next
        
        listNum.sort()
        
        curr = head
        i = 0
        while curr != None:
            curr.val = listNum[i]
            curr = curr.next
            i+=1
        return head
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        