# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current_node = head
        if current_node:
            next_node = current_node.next
        else:
            return head

        while next_node != None:
            print(next_node.val)
            temp = next_node
            next_node = next_node.next
            temp.next = current_node
            current_node = temp
            head.next = None
        head = current_node


        return head


    # 0 1 2 3

    # 0 = current


    # 0 = previous
    # 1 = current


    # need 1 .next to be 0