class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        length = len(matrix) * len(matrix[0]) - 1
        
        height = len(matrix)
        width = len(matrix[0])
        print("height")
        print(height)
        print("width")
        print(width)

        left = 0
        right = length

        i = 0
        j = 0


        while left <= right and right >= 0:

            mid = (left + right) // 2
            print("mid: " + str(mid))
            print("mid//height: "+ str(mid//height))
            print("mid%height: "+ str(mid%height))

            n = matrix[mid//width][mid%width]
            # n = matrix[mid%height][mid//height]

            print(n)

            if n == target:
                return True
            
            elif n < target:
                left = mid + 1
            
            else:
                right = mid - 1

        return False



