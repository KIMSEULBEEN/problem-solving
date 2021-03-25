def solution(num, BFs):
    answer = []

    # 0. 좌표평면 만들기
    C = [[0 for _ in range(num+1)] for _ in range(num+1)]

    # 1. 기둥, 보 설치 & 삭제
    for n, BF in enumerate(BFs):
        #print(n, answer, "BF: ", BF)
        x, y, a, b = BF
        # 1) 일단 설치 or 삭제
        def install_remove(C, BF):
            if b == 1:
                answer.append(BF[:-1])
                # (1) 기둥일 경우
                if a == 0: C[y][x] += 10
                # (2) 보일 경우
                else: C[y][x] += 1
            else:
                answer.remove(BF[:-1])
                # (1) 기둥일 경우
                if a == 0: C[y][x] -= 10
                # (2) 보일 경우
                else: C[y][x] -= 1
            return C, answer
            # 설치 or 삭제
        C, answer = install_remove(C, BF)

        # 2) 설치 or 삭제 후 규칙을 만족하면 그대로 두고 아니면 삭제
        def qulify_rule(C, answer):
            for n, BF in enumerate(answer):
                x, y, a = BF
                # (1) 기둥일 경우
                if a == 0:
                    # a) y가 0보가 크고
                    if y > 0:
                        # (a) 아래 기둥이 없을 경우
                        if C[y-1][x]//10 == 0:
                            # ㄱ) 아래 보가 없을 경우 False
                            if C[y][x - 1] % 10 == 0 and C[y][x] % 10 == 0: return False

                # (2) 보일 경우
                else:
                    # a) 양쪽 아래 기둥이 없고 양쪽에 보가 없을 경우 False
                    if C[y-1][x]//10 == 0 and C[y-1][x+1] // 10 == 0:
                        if C[y][x-1] % 10 == 0 or C[y][x+1] % 10 == 0: return False

            # for문 돌렸을 때 False가 나오지 않았을 경우 True 리턴
            return True

        if qulify_rule(C, answer) == False:
            def install_remove_rev(C, BF):
                if b == 0:
                    answer.append(BF[:-1])
                    # (1) 기둥일 경우
                    if a == 0:
                        C[y][x] += 10
                    # (2) 보일 경우
                    else:
                        C[y][x] += 1
                else:
                    answer.remove(BF[:-1])
                    # (1) 기둥일 경우
                    if a == 0:
                        C[y][x] -= 10
                    # (2) 보일 경우
                    else:
                        C[y][x] -= 1
                return C, answer
            C, answer =  install_remove_rev(C, BF)
        answer.sort()

    return answer
