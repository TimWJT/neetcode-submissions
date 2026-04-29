# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False
        slow_pointer = head
        fast_pointer = head.next

        while slow_pointer != None and fast_pointer != None:
            print(slow_pointer.val)
            print(fast_pointer.val)
            if fast_pointer == slow_pointer:
                print(slow_pointer.val)
                print(fast_pointer.val)
                return True

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            if fast_pointer != None:
                fast_pointer = fast_pointer.next
            else:
                return False
            
        return False
