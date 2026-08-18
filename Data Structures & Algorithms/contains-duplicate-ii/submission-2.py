class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        left = 0 
        right = 0
        res = {}

        while right < len(nums):

            #right
            if nums[right] not in res:
                res[nums[right]] = 0
            
            res[nums[right]] += 1
            if res[nums[right]] >= 2:
                return True

            

            if abs(left - right) < k:
                right += 1
            else:
                right += 1

                res[nums[left]] -= 1
                left += 1



        return False