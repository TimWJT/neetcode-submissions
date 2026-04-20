class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while i < index and current:
            current = current.next
            i +=1

        if current:
            return current.val
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node
        

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)

        else:

            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = Node(val)
        
        

    # def remove(self, index: int) -> bool:
    #     if not self.head:
    #         return False

    #     if index == 0 and self.head:
    #         self.head = self.head.next
    #         return True
        

    #     current = self.head
    #     i = 0
    #     while i < index -1:
    #         current = current.next
    #         i +=1


    #     to_remove = current.next
    #     if to_remove.next:
    #         current.next = to_remove.next
    #     else:
    #         current.next = None            
    #     return True
    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            return False
        
        current = self.head
        i = 0
        while i < index - 1 and current:
            current = current.next
            i += 1

        if current and current.next:  # ← Check both exist!
            to_remove = current.next
            if to_remove.next:
                current.next = to_remove.next
            else:
                current.next = None            
            return True
        
        return False

            
                
            

    def getValues(self) -> List[int]:

        array = []
        current = self.head
        
        while current != None:
            array.append(current.val) 
            current = current.next
        return array

        

class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None










