class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        if self.array[i] == None:
            self.size +=1

        self.array[i] = n


    def pushback(self, n: int) -> None:

        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = n
        self.size+=1


        # i = 1
        # while self.array[-i] == None:
        #     i +=1
        # if i == 0:
        #     self.resize()
        #     self.array[self.capacity] = n
        # else:
        #     self.array[-i] = n

        
        # self.array[-1] = self.array[n]
        # self.array[n] = None


    def popback(self) -> int:
        pop_value = self.array[self.size-1]

        self.array[self.size-1] = None
        self.size -=1
        return pop_value



    def resize(self) -> None:
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i, n in enumerate(self.array):
            new_array[i] = n
        self.array = new_array

    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
