class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        answer = []
        
        while head:
            answer.append(head.val)
            head = head.next
        
        return answer == answer[::-1]