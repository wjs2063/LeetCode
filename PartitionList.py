# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        up=deque([])
        down=deque([])
        
        while head:
            n=head.val
            if n<x:
                down.append(n)
            else:
                up.append(n)
            head=head.next
        start=head=ListNode()
        while down:
            x=down.popleft()
            head.next=ListNode(x)
            head=head.next
        while up:
            x=up.popleft()
            head.next=ListNode(x)
            head=head.next
        return start.next
            