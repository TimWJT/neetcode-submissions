class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        already_appear = set()

        for i in range(len(nums)):
            if nums[i] in already_appear:
                return True
            else:
                already_appear.add(nums[i])
        return False