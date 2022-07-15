"""
백준 2293번 동전 1
n: 동전 종류
k: 가치의 합
"""

from collections import deque
from copy import deepcopy

class Coin:
    def __init__(self):
        self.answer = 0

    def get_answer(self, number, coins):
        """
        동전 소액권을 하나씩 제거해가면서 number를 줄여나간다.
        남은 number가 0일 경우 answer + 1
        :param number: 잔여 숫자
        :param coins: 잔여 코인들
        :return: answer
        """

        if len(coins) > 0:
            coin_value = coins.popleft()

            num_iterates = number // coin_value
            for idx in range(0, num_iterates + 1):
                number_cpr = coin_value * idx

                number_left = number - number_cpr
                # print(number_left, coins, coin_value, idx, num_iterates)
                if number_left > 0:
                    self.get_answer(number_left, deepcopy(coins))

                # 잔여숫자 0일 경우 번호 추가
                elif number_left == 0:
                    self.answer += 1






coins = deque([3, 6])
coin = Coin()
coin.get_answer(6, coins)
print(coin.answer)