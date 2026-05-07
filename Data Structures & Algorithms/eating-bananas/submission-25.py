from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest_pile = max(piles)

        left = 1
        right = largest_pile

        while left < right and right >= 1 and left <= largest_pile and left != right:

            mid = ((left + right) // 2)

            #simulate

            h_count = h
            print("mid")
            print(mid)
            for p in piles:

                h_count -= ceil(p/mid)

            print("hcount")
            print(h_count)
           
            if h_count >= 0:
                right = mid

            elif h_count < 0:
                left = mid + 1

        if h_count >=0:

            return mid
        else:
            return mid + 1

                

                

