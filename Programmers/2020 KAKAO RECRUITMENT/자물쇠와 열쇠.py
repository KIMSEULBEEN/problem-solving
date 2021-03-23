import copy

def solution(K, L):
    lenK, lenL = len(K), len(L)
    answer = False

    # 0. 필요 함수
    #  1) rotate_90: 90도 이동 함수
    def rotate_90(K):
        lenK = len(K)
        T = [[0] * lenK for n in range(lenK)]
        for h in range(lenK):
            for w in range(lenK):
                T[h][lenK - 1 - w] = K[w][h]
        return T


    #   2) make_largeL: 열쇠 확인용 확장 2차원 배열 생성 함수
    def make_largeL(lenK, L):
        lenL = len(L)
        lenLp = 2*lenK + lenL
        Lp = [[0] * lenLp for n in range(lenLp)]

        for h in range(lenK, lenK+lenL):
            for w in range(lenK, lenK+lenL):
                Lp[h][w] = L[h-lenK][w-lenK]
        return Lp

    #   3) check_unlock: 열쇠로 자물쇠를 풀 수 있는지 확인하는 함수
    def check_unlock(K, Lp):
        Lp_ori = copy.deepcopy(Lp)
        check_flag = False
        # 열쇠와 자물쇠 배열이 겹치는 구간까지 for문 설계
        for h in range(lenK + lenL):
            for w in range(lenK + lenL):
                Lp = copy.deepcopy(Lp_ori)
                # 부분더하기 함수
                def sum_part(K, Lp, h, w):
                    for _h in range(lenK):
                        for _w in range(lenK):
                            Lp[h+_h][w+_w] += K[_h][_w]
                    return Lp
                Lp = sum_part(K, Lp, h, w)
                Lp_part = [semiLp[lenK:lenK + lenL] for semiLp in Lp[lenK:lenK+lenL]]

                K_part = [semiK[:2] for semiK in K[:2]]
                if max(sum(Lp_part, [])) == 1 and min(sum(Lp_part, [])) == 1:
                    check_flag = True
                    break
        return check_flag

    # 1. 확장 2차원 배열, 90도 이동 함수 4개 생성
    K_LIST = [K]
    for n in range(3): K_LIST.append(rotate_90(K_LIST[-1]))
    Lp = make_largeL(lenK, L)

    # 2. K1, K2, K3, K4에 대해 확인
    for Kt in K_LIST:
        if check_unlock(Kt, Lp):
            answer = True
            break

    return answer
