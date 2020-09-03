from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices = []
        max_price = 0
        for i in prices[::-1]:
            if i > max_price:
                max_price = i
            max_prices.append(max_price)

        max_profit = 0
        max_prices.reverse()
        for i in range(len(prices)):
            cur_profit = max_prices[i] - prices[i]
            if cur_profit > max_profit:
                max_profit = cur_profit

        return max_profit
