"""
BOJ 1018 체스판 다시 칠하기
"""

def check_chess(matrix, hei, wid):
    answer1 = 0
    answer2 = 0
    for h in range(hei, hei + 8):
        for w in range(wid, wid + 8):
            # w + h
            is_black_gt = (w+h)%2 == 0
            is_black = True if matrix[h][w] == "B" else False
            if is_black != is_black_gt:
                answer1 += 1

            # w + h
            is_black_gt = (w + h) % 2 == 1
            is_black = True if matrix[h][w] == "B" else False
            if is_black != is_black_gt:
                answer2 += 1

    return min(answer1, answer2)


height, width = list(map(int, input().split()))
matrix_ori = [input() for _ in range(height)]

answer = height * width
for h in range(height - 8 + 1):
    for w in range(width - 8 + 1):
        answer_tmp = check_chess(matrix_ori, h, w)
        answer = min(answer, answer_tmp)
        if answer == 0:
            break
    if answer == 0:
        break

print(answer)