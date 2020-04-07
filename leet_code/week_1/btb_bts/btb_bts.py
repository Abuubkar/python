# Best time to Buy & Best time to Sell
import numpy as np


class Solution:
    def maxProfit(self, prices: [int]):

        i = 0
        j = 0
        size = len(prices)
        max_profit = 0
        while j < size:
            j = i+1
            if j >= size:
                break
            curr_profit = prices[j] - prices[i]
            if curr_profit > 0:
                max_profit += curr_profit

            i += 1
        print(max_profit)


solution = Solution()
with open('./input.txt', 'r') as file:
    lines = file.readlines()
    for case in range(len(lines)):
        input_array = np.array(list(map(int, lines[case].split(','))))
        solution.maxProfit(input_array)
