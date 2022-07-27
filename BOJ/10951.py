"""
BOJ 10951 A + B - 4
"""

while True:
    try:
        a, b = list(map(int, input().split(' ')))
        print(a + b)
    except EOFError:
        break
