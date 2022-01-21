"""
백준 2045 마방진

입력
magic_square: 마방진 (3*3, int)
sum_square: 마방진 합
"""
import sys

# 0. 입력 받기
magic_square = []
for _ in range(3):
    row = list(map(int,  input().split(' ')))
    magic_square.append(row)


# 1. 합계 파악
#   각 행, 열을 탐색하여 0을 포함하지 않는 경우를 탐색

sum_square = 0
#   1) 행 합계
for idx in range(3):
    if sum_square > 0: break

    if min(magic_square[idx]) > 0:
        sum_square = sum(magic_square[idx])

#   2) 열 합계
for idx_col in range(3):
    if sum_square > 0: break

    sum_num = 0
    min_num = sys.maxsize
    for idx_row in range(3):
        sum_num += magic_square[idx_row][idx_col]
        min_num = min(min_num, magic_square[idx_row][idx_col])
    if min_num > 0:
        sum_square = sum_num

#    3) 대각선 합계
if sum_square == 0:
    sum_num = 0
    min_num = sys.maxsize
    for idx in range(3):
        if sum_square > 0: break

        sum_num += magic_square[idx][idx]
        min_num = min(min_num, magic_square[idx][idx])

    if sum_square == 0 and min_num > 0:
        sum_square = sum_num

    sum_num = 0
    min_num = sys.maxsize
    for idx in range(3):
        if sum_square > 0: break

        sum_num += magic_square[idx][2 - idx]
        min_num = min(min_num, magic_square[idx][2 - idx])

    if sum_square == 0 and min_num > 0:
        sum_square = sum_num

# print(sum_square)

# 2. 마방진 채우기
#   각 행, 열을 탐색하여 0을 포함하지 않는 경우가 1개일 경우 마방진 채움

#   1) 행 채우기
if sum_square == 0:
    if magic_square[0][0] == 0: # 왼쪽 위 대각선
        num_gijun = 0
        sum_gijun = sum(magic_square[0])


        sum_tmp = 0
        for idx in range(1, 3): # 1, 2
            sum_tmp += sum(magic_square[idx]) - sum(magic_square[0])
        num_gijun = (sum_tmp + sum(magic_square[0])) // 2
        print(num_gijun)

        magic_square[0][0] = num_gijun
        for idx in range(1, 3):
            magic_square[idx][idx] = sum(magic_square[0]) - sum(magic_square[idx])

    else:
        num_gijun = 0
        sum_gijun = sum(magic_square[0])


        sum_tmp = 0
        for idx in range(1, 3):
            sum_tmp += sum(magic_square[idx]) - sum_gijun
        num_gijun = (sum_tmp + sum(magic_square[0])) // 2
        # print(num_gijun)

        magic_square[0][2] = num_gijun
        for idx in range(1, 3):
            magic_square[idx][2 - idx] = sum(magic_square[0]) - sum(magic_square[idx])

else:

    for idx_row in range(3):
        is_fill = True
        sum_square_cpr = 0
        idx_row_0, idx_col_0 = -1, -1
        for idx_col in range(3):
            sum_square_cpr += magic_square[idx_row][idx_col]
            if magic_square[idx_row][idx_col] == 0:
                if idx_row_0 != -1:
                    # print(idx_row, idx_col)
                    is_fill = False
                    break # 0이 이미 나와서 초기값이 -1이 아닐 경우 pass
                else:
                    idx_row_0 = idx_row
                    idx_col_0 = idx_col

        if is_fill and idx_row_0 != -1:
            magic_square[idx_row_0][idx_col_0] = sum_square - sum_square_cpr

    #   2) 열 채우기
    for idx_col in range(3):
        is_fill = True
        sum_square_cpr = 0
        idx_row_0, idx_col_0 = -1, -1
        for idx_row in range(3):
            sum_square_cpr += magic_square[idx_row][idx_col]
            if magic_square[idx_row][idx_col] == 0:
                if idx_row_0 != -1:
                    is_fill = False
                    break # 0이 이미 나와서 초기값이 -1이 아닐 경우 pass
                else:
                    idx_row_0 = idx_row
                    idx_col_0 = idx_col

        if is_fill and idx_row_0 != -1:
            magic_square[idx_row_0][idx_col_0] = sum_square - sum_square_cpr




for rows in magic_square:
    print(*rows)
