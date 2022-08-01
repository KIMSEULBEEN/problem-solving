"""
BOJ 1120 문자열
"""

A, B = input().split()
len_A, len_B = len(A), len(B)
loops = len_B - len_A

diff_min = len_B
for idx_b in range(loops + 1):
    diff = 0
    for idx in range(len_A):
        if A[idx] != B[idx + idx_b]:
            diff += 1
    diff_min = min(diff, diff_min)

print(diff_min)