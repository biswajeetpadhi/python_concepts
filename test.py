def coinChange(coins, amount):
    # Recursive helper function
    def helper(coins, amount):
        # Base cases
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        
        # Initialize minimum number of coins to a large value
        min_coins = float('inf')
        
        # Try all coin denominations
        for coin in coins:
            res = helper(coins, amount - coin)
            if res >= 0:
                min_coins = min(min_coins, res + 1)

        if min_coins != float('inf'):
            return min_coins
        else:
            return -1

    # Call the recursive helper function
    return helper(coins, amount)


coins = [1,2,5]
amount = 6
print(coinChange(coins, amount))