class BuySellStock:
    def singlebuy(prices):
        ## buy and sell once  
        buy = prices[0]
        max_profit = 0
        profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            if profit < 0:
                buy = prices[i]
            max_profit = max(profit, max_profit)
        return max_profit

    def unlimitedbuys(prices):
        ## buy and sell unlimited times
        max_profit = 0
        profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit
        return max_profit

    def max2buys(prices):
        ## can buy a max of 2 times cannot buy on the day sold
        n = len(prices)
        left = [0] * n ## max profit to the left of index including current
        min_to_left = prices[0]
        max_profit_left = left[0]
        for i in range(1, n):
            max_profit_left = max(prices[i] - min_to_left, max_profit_left)
            left[i] = max_profit_left
            min_to_left = min(min_to_left, prices[i])
        
        right = [0] * n ## max profit to the right of index including current
        max_to_right = prices[-1]
        max_profit_right = right[-1]
        for i in range(n - 2, -1, -1):
            max_profit_right = max(max_to_right - prices[i], max_profit_right)
            right[i] = max_profit_right
            max_to_right = max(prices[i], max_to_right)
        
        mixed_profits = [0] * n
        for i in range(n):
            mixed_profits[i] = left[i] + (right[i + 1] if i < n- 1 else 0)

        return max(mixed_profits)







                

