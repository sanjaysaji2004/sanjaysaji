list1= [10, 22, 5, 75, 65, 80]
def max_profit(prices):
    n = len(prices)
    # Initialize dp array with 0 values
    dp = [0] * n
    # Initialize variables to keep track of minimum price and maximum profit
    min_price = prices[0]
    max_profit = 0
    # First transaction
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
        dp[i] = max_profit
    # Second transaction
    max_price = prices[n-1]
    max_profit = 0
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, max_price - prices[i] + dp[i])
    return max_profit
print(max_profit(list1))
