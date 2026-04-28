class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        high = prices[0]
        low = prices[0]
        largest_profit = 0

        for i, n in enumerate(prices):

            
            print(n)

            if n <= low:
                print("new low")
                low = n
                high = 0

            if n > high:
                high = n
                print("largest profit: " + str(largest_profit))

            if high - low > largest_profit:
                largest_profit = high - low

        return largest_profit
        


# 2 9 1 7 4 10