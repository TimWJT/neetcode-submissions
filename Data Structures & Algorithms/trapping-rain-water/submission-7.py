class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        left = 0
        right = 0
        total_volume = 0
        local_volume = 0

        while right < len(height):

            if height[right] >= height[left]:
                total_volume += local_volume
                print(local_volume)
                local_volume = 0
                left = right
                right += 1
                continue

            local_volume += height[left] - height[right]
            right += 1

        stop_location = left
        local_volume = 0

        left = len(height) - 1
        right = len(height) - 1

        while left >= stop_location:

            if height[left] >= height[right]:
                total_volume += local_volume
                local_volume = 0
                right = left
                left -= 1
                continue
            local_volume += height[right] - height[left]
            left -= 1
            # if right - left < 0:
            #     right += 1
            #     continue

            # volume = min(height[left], height[right]) * 
        return total_volume



