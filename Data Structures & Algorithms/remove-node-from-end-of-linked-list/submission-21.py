# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # if n == 0:
        #     return head.next
        # elif n == 1:
        #     head.next = None
        #     return None


        # count linked list length
        current = head
        list_length = 0

        while current:
            list_length += 1
            current = current.next

        print(list_length)

        
        index = 0
        previous = None
        current = head

        print("test")

        while current != None:
            print(current.val)
            print(index)

            needed_index = list_length - n



            if index == needed_index:

                if needed_index == 0:
                    if head != None:
                        head = head.next
                        return head
                    
                    else:
                        return None

                
              
                previous.next = current.next




            index += 1
            previous = current
            current = current.next


        
        return head