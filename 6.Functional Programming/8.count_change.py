def count_change(coins, amount):
    # Create a list to store the number of ways to make change for each amount
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is one way to make change for 0 amount (using no coins)

    # Iterate over each coin
    for coin in coins:
        # Update the dp list for all amounts from coin to amount
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]


coins = [1, 2, 3]
amount = 4
print(f"Number of ways to make change for {amount} using {coins}: {count_change(coins, amount)}")
