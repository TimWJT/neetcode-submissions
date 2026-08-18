class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}
        for i, n in enumerate(nums):
            
            if n not in res:

                res[target - n] = i
            
            else:
                return [res[n], i]