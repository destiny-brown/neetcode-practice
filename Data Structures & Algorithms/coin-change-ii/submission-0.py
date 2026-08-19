class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        distinct_combs = [0] * (amount + 1)

        distinct_combs[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                distinct_combs[i] += distinct_combs[i - coin]
        
        return distinct_combs[amount]
        