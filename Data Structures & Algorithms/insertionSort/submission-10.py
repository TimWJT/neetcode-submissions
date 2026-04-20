# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []
        
        for i, n in enumerate(pairs):
            if i == 0:
                output.append(pairs[:])
                continue

            j = i - 1
            while j >= 0 and n.key < pairs[j].key:
                pairs[j + 1] = pairs[j]  # Shift right
                j -= 1
            pairs[j + 1] = n  # Insert at correct position
            output.append(pairs[:])  # Copy!
        
        return output
        

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
# #         self.value = value
# class Solution:
#     def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
#         output = []
        
#         for i in range(len(pairs)):
#             j = i - 1
#             # Move elements that are greater than key one position ahead
#             while j >= 0 and pairs[j].key > pairs[j + 1].key:
#                 pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
#                 j -= 1
            
#             # Clone and save the entire state of the array at this point
#             output.append(pairs[:])
        
#         return output








            