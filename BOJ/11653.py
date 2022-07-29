"""
BOJ 11653 소인수분해
"""

N = int(input())

N_div = N
for num in range(2, N + 1):
    while N_div % num == 0:
        print(num)
        N_div = N_div // num

    if N_div == 1:
        break