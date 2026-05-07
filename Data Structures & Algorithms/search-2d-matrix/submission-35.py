class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        length = len(matrix) * len(matrix[0]) - 1
        
        height = len(matrix)
        width = len(matrix[0])
     

        left = 0
        right = length

        i = 0
        j = 0


        while left <= right and right >= 0:

            mid = (left + right) // 2
         
            n = matrix[mid//width][mid%width]


            if n == target:
                return True
            
            elif n < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return False



