class Solution:
    def maxArea(self, heights: List[int]) -> int:
        


        largest_area = 0


        left = 0
        right = len(heights) - 1

        while left < right and left < len(heights) and right > 0:
            print("left: " + str(heights[left]))
            print("right: " + str(heights[right]))
            x = right - left
            y = min(heights[left], heights[right])
            
            area = x * y

            if area > largest_area:
                largest_area = area

                print("x: " + str(x))
                print("y: " + str(y))
                print("largest a: " + str(largest_area))
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            

            
        return largest_area