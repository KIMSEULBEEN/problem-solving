"""
BOJ 2609 최대공약수와 최소공배수
"""

num1, num2 = list(map(int, input().split(' ')))

import math

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))