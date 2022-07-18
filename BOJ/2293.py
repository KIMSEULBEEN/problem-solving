"""
백준 2293번 동전 1
n: 동전 종류
k: 가치의 합
"""

from collections import deque
from copy import deepcopy

"""
dp size: len(coins) * number 
행 크기: len(coins)
열 크기: number
dp[r][c]: coins[0] ~ coins[r] 코인을 활용하여 만들 수 있는 조합의 수
        = dp[r][c - coins[r]] + dp[r - 1][c - coins[r]] .... + dp[0][c - coins[r]]
"""
class Coin:
    def __init__(self, number, coins):
        self.number = number
        self.coins = coins
        # self.dp = [[0] * (number + 1) for _ in range(len(self.coins))]
        self.dp = [0] * (number + 1)
        self.answer = 0


    def get_answer(self):
        self.dp[0] = 1

        # 코인별 반복문
        for coin in coins:
            for num in range(number + 1):
                if num // coin > 0:
                    idx = num - coin
                    self.dp[num] += self.dp[idx]


        self.answer = self.dp[-1]
        return self.answer


len_coin, number  = list(map(int, input().split(' ')))
coins = []

import sys
for _ in range(len_coin):
    coin = int(sys.stdin.readline())
    coins.append(coin)

coin = Coin(number, coins)
print(coin.get_answer())
# print(coin.dp)



