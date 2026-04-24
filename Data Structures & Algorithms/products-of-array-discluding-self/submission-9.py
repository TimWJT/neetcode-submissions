class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total_product = 1.0
        zero_counter = 0


        for n in nums:
            if n == 0:
                zero_counter +=1
            else:
                total_product *= n
            
        

        for n in nums:
            
            if zero_counter > 0 and n != 0:
                output.append(0)
            
            elif zero_counter == 1 and n == 0:
                output.append(int(total_product))
            
            elif zero_counter > 1:
                output.append(0)

            else:
                output.append(int(total_product/n))


        
        return output