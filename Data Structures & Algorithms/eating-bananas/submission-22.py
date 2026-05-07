from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest_pile = max(piles)

        left = 1
        right = largest_pile

        # Simplified while condition to prevent crashes/logic errors
        while left < right:

            mid = (left + right) // 2

            # simulate
            h_count = h
            for p in piles:
                h_count -= ceil(p/mid)
            
            if h_count >= 0:
                # This speed works, try to find a smaller one
                right = mid
            else:
                # Too slow, must increase speed
                left = mid + 1

        # When left == right, we've found the minimum speed
        return left