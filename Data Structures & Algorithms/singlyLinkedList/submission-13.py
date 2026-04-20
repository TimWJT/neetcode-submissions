class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while current and i < index:
            current = current.next
            i += 1
        
        if current:
            return current.val
        return -1
    
    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(val)
    
    def remove(self, index: int) -> bool:
        if index == 0 and self.head:
            self.head = self.head.next
            return True
        
        current = self.head
        i = 0
        while current and i < index - 1:
            current = current.next
            i += 1
        
        if current and current.next:
            current.next = current.next.next
            return True
        return False
    
    def getValues(self) -> List[int]:
        array = []
        current = self.head
        while current is not None:
            array.append(current.val)
            current = current.next
        return array