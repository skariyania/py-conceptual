"""
Best Time to Buy and Sell Stock 
You are given an array prices.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""
class Solution(object):
    """ class implementing maximum profit solution """
    def max_profit(self, prices):
        """ method implements maximum profit solution """
        min_val_p = 0
        max_val_p = 1
        max_profit = 0
        while max_val_p < len(prices):
            profit = prices[max_val_p] - prices[min_val_p]
            if prices[min_val_p] < prices[max_val_p]:
                max_profit = max(profit, max_profit)
            else:
                min_val_p = max_val_p
            max_val_p += 1
        return max_profit

if __name__ == "__main__":
    input_values = [7,6,4,3,1]
    res = Solution().maxProfit(prices=input_values)
    print(res)
