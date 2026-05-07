class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


        max_per_window = []

        left = 0
        right = k-1

        while right < len(nums):

            # current_window = []
            # i = 0

            # while i < right:

            #     i += 1
            max_per_window.append(max(nums[left:right+1]))

            left += 1
            right += 1

        return max_per_window