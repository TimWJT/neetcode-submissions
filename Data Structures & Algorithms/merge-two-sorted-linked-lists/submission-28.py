# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        return_list_head = ListNode()
        current_return_list = return_list_head

        current_list1 = list1
        current_list2 = list2
        
        

        while current_list1 != None and current_list2 != None:
            new_node = ListNode()
            if current_list1.val < current_list2.val:

                new_node.val = current_list1.val
                current_list1 = current_list1.next
            
            else:
                new_node.val = current_list2.val
                current_list2 = current_list2.next
            
            # print(current_return_list.val)
            current_return_list.next = new_node
            current_return_list = new_node
        if current_list1:
            print(current_list1.val)
            print("printing from 1")
            current_return_list.next = current_list1
        if current_list2:
            print(current_list2.val)
            print("printing from 2")



            current_return_list.next = current_list2


        
        return return_list_head.next

