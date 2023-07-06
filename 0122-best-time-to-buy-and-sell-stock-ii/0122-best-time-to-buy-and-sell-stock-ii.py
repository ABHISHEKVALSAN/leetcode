class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        n = len(prices)
        profit = 0
        while i < n-1:
            if prices[i] < prices[i+1]:
                profit += (prices[i+1]-prices[i])
            i+=1
        return profit