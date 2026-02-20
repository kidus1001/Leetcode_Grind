# I didn't use insertion sort tho. (As the question suggests)
class Solution(object):
    def insertionSortList(self, head):
        listNum = []
        curr = head
        while curr is not None:
            listNum.append(curr.val)
            curr = curr.next
        
        listNum.sort()
        curr = head
        i = 0
        while curr is not None:
            curr.val = listNum[i]
            curr = curr.next
            i+=1
        
        return head
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        