class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_fut = []
        max_price = -1
        n = len(prices)
        i = n-1
        while i>=0:
            max_price = max(max_price,prices[i])
            max_fut.append(max_price)
            i-=1

        max_fut = max_fut[::-1]

        profit = 0
        i = 0 
        while i<n-1:
            price = prices[i]
            profit = max(profit, max_fut[i+1]-price)
            i+=1
        return profit
