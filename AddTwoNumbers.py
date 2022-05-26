# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=""
        while l1:
            x=str(l1.val)
            str1+=x
            l1=l1.next
        str2=""
        while l2:
            x=str(l2.val)
            str2+=x
            l2=l2.next
        str3=str(int(str1[::-1])+int(str2[::-1]))[::-1]
        #node create
        a=n=ListNode()
        #start node : a
        for x in str3:
            n.next=ListNode()
            n=n.next
            n.val=int(x)
        
        return a.next # first node.val is 0 
