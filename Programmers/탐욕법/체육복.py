def solution(n, lost, reserve):
    n_num = [1] * (n + 1)
    n_num[0] = -1

    for i in lost: n_num[i] -= 1
    for i in reserve: n_num[i] += 1

    n_num_res, n_num_lost = [], []
    for i in range(n + 1):
        if n_num[i] == 2: n_num_res.append(i)
        elif n_num[i] == 0: n_num_lost.append(i)


    for i in range(len(n_num_lost)):
        for j in range(len(n_num_res)):
            idx_lost, idx_res = n_num_lost[i], n_num_res[j]
            # print(idx_lost, idx_res)
            if abs(idx_lost-idx_res) <= 1:
                # print(i,j)
                n_num[idx_lost] += 1
                n_num[idx_res] -= 1
                n_num_lost[i] = -10
                n_num_res[j] = -15

    result = 0
    for i in n_num:
        if i > 0: result += 1
    return result
