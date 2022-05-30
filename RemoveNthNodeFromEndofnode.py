# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        
        start=head
        
        while head:
            if head!=None:
                length+=1
            head=head.next
        #case first=last=removenode
        if length==1 and n==1:
            return None
        #case remove last node
        head=start
        cnt=0
        if n==length:
            return head.next
        while start:
            if start!=None:
                cnt+=1
            # example length=5, n=2 we find third node 
            if cnt==(length-n):
                if n==1:
                    start.next=None
                    break
                else:
                    start.next=start.next.next
                    break
            start=start.next
        return head
                        