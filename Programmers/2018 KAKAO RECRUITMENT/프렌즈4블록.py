def solution(m, n, board):
    cnt_delete = 0
    width, height = n, m
    B = [list(n) for n in board]

    while True:
        def remove_block(B):
            DC = []
            # 첫쨰 줄부터 마지막 전 줄까지
            for h in range(height - 1):
                # 둘째 항부터 마지막 전 항까지
                for w in range(1, width - 1):
                    c = B[h][w]
                    if B[h][w] == c and B[h+1][w] == c:
                        # 오른쪽 아래 네모
                        if B[h][w+1] == c and B[h+1][w+1] == c:
                            for _arr in [[h, w], [h+1, w], [h, w+1], [h+1, w+1]]: DC.append(_arr)
                        # 왼쪽 아래 네모
                        if B[h][w-1] == c and B[h+1][w-1] == c:
                            for _arr in [[h, w], [h+1, w], [h, w-1], [h+1, w-1]]: DC.append(_arr)
            cnt = 0
            for h, w in DC:
                if B[h][w] != '0':
                    B[h][w] = '0'
                    cnt += 1
            return cnt, B

        cnt, B = remove_block(B)
        cnt_delete += cnt
        if cnt == 0: break

        def arrange_board(B):
            # 밑에서 두 번쨰 줄부터 첫 번째 줄까지
            for h in range(height - 2, -1, -1):
                # 전부 다
                for w in range(width):
                    # 0이 아닐 경우
                    if B[h][w] != '0':
                        h_plus = 1
                        while h + h_plus < height:
                            # 아래 픽셀값이 0일 경우
                            if B[h + h_plus][w] == '0': h_plus += 1 # 아래로 1만큼 더 전진
                            else: break
                        if h_plus > 1: B[h][w], B[h + h_plus - 1][w] = '0', B[h][w]

            return B
        B = arrange_board(B)

    return cnt_delete
