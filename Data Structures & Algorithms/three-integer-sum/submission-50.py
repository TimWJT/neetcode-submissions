class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        nums = sorted(nums)

        previous_n = None

        for index, n in enumerate(nums):

            if n == previous_n:
                continue
            previous_n = n

            left = index
            right = len(nums) - 1

            while left < len(nums) and right > index and left < right:
                if left == index:
                    left += 1
                    continue

                if right == index:
                    right -= 1
                    continue

                if nums[left] + nums[right] == -n:
                    output.append([n, nums[left], nums[right]])

                    while left < len(nums)-1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > index and nums[right] == nums[right - 1]:
                        right -= 1

                    # CHANGED: step off the matched pair so we don't re-match it forever
                    left += 1
                    right -= 1

                else:
                    # CHANGED: this if/else is now INSIDE the else block
                    # (indented one level deeper than before)
                    if nums[left] + nums[right] < -n:
                        left += 1
                    else:
                        right -= 1

        return output