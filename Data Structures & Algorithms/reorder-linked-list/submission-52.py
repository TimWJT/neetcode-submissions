# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # bruet force



        nodes = []


        next_n = head
        while next_n != None:
            
            nodes.append(next_n)
            next_n = next_n.next

        
        i = 0
        j = len(nodes) - 1
        while i <= j:
            
            print(nodes[i].val)
            print(nodes[j].val)
            print("value of i: " + str(i))
            print("value of j: " + str(j))


            nodes[i].next = nodes[j]
            if i + 1 == j or i == j:
                nodes[j].next = None
                break
                
            nodes[j].next = nodes[i + 1]

            i += 1
            j -= 1
        