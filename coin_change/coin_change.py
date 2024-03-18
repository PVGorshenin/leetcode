from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        just_big_number = 100500
        dp_list = [just_big_number] * (amount + 1)
        dp_list[0] = 0

        result = self.dp(coins, amount, dp_list)

        if result == just_big_number:
            return -1
        return result

    def dp(self, coins, amount, dp_list):

        for i_dp in range(1, amount+1):

            for coin in coins:

                if i_dp % coin == 0:
                    n_curr_coins = i_dp // coin
                    dp_list[i_dp] = min(dp_list[i_dp], n_curr_coins)

                if i_dp - coin >= 0:
                    dp_list[i_dp] = min(dp_list[i_dp], dp_list[i_dp-coin]+1)

        return dp_list[amount]




coins = [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422]

print(Solution().coinChange(coins, 9864))




