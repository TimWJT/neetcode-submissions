class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        
        i = 0
        j = 0


        while i < len(nums):
            j = i
            while j < len(nums):                    

                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

                j += 1
            i += 1