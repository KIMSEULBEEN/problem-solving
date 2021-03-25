from itertools import combinations
import copy

def solution(num_walls, W, P):
    for p in range(1, len(P) + 1):
        COMBS = list(combinations(W, p))

        for COMB in COMBS:
            W_copy = copy.deepcopy(W)
            def cal_T(W_copy, COMB):
                # 정방향
                T1 = []
                for n, c in enumerate(COMB):
                    if n == 0:
                        Wt = W_copy[W_copy.index(c):] + W_copy[:W_copy.index(c)]
                    if n + 1 != len(COMB):
                        t = Wt[Wt.index(COMB[n+1]) - 1] - Wt[Wt.index(COMB[n])]
                        if t == 0: t = 1
                        if t < 0: t += num_walls
                        T1.append(t)
                    else:
                        t = Wt[-1] - Wt[Wt.index(COMB[n])]
                        if t == 0: t = 1
                        if t < 0: t += num_walls
                        T1.append(t)

                # 역방향
                W_copy.reverse()
                # 역방향
                T2 = []
                for n, c in enumerate(COMB):
                    if n == 0:
                        Wt = W_copy[W_copy.index(c):] + W_copy[:W_copy.index(c)]
                    if n + 1 != len(COMB):
                        t = Wt[Wt.index(COMB[n + 1]) - 1] - Wt[Wt.index(COMB[n])]
                        if t == 0: t = -1
                        if t > 0: t -= num_walls
                        T2.append(-t)
                    else:
                        t = Wt[-1] - Wt[Wt.index(COMB[n])]
                        if t == 0: t = -1
                        if t > 0: t -= num_walls
                        T2.append(-t)

                return T1, T2
            T1, T2 = cal_T(W_copy, COMB)

            def check_repair(T, P):
                T, P = sorted(T), P[-p:]
                for n in range(p):
                    if T[n] > P[n]: return False
                return True

            if check_repair(T1, P): return p
            if check_repair(T2, P): return p
    return -1
