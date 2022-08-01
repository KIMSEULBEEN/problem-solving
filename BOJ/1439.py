"""
BOJ 1439 뒤집기
"""

S = input().rstrip()

while True:
    len_S_s = len(S)

    S = S.replace("11", "1")
    S = S.replace("00", "0")

    len_S_e = len(S)

    if len_S_s == len_S_e:
        break

# print(S)
print(min(S.count('1'), S.count('0')))