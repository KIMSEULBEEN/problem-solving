def rotate_wise(G, r):
    if r == 1: # 시계
        G.insert(0, G.pop())
    elif r == -1: # 반시계
        G.append(G.pop(0))
    return G

G = []
for n in range(4): G.append(list(input()))

num_r = int(input())
for n in range(num_r):
    R = [0, 0, 0, 0]
    idx, r = input().split(' ')
    idx, r = int(idx) - 1, int(r)

    R[idx] = r


    # 오른쪽으로
    idx_plus = idx
    while idx_plus < len(G) - 1:
        if idx_plus >= len(G) - 1: break

        if G[idx_plus][2] != G[idx_plus+1][6]:
            R[idx_plus+1] = R[idx_plus] * -1
        idx_plus += 1

    # 왼쪽으로
    idx_minus = idx
    while idx_minus > 0:
        if idx_minus <= 0: break

        if G[idx_minus][6] != G[idx_minus-1][2]:
            R[idx_minus-1] = R[idx_minus] * -1
        idx_minus -= 1


    # 맞추어 회전
    for m in range(4):
        G[m] = rotate_wise(G[m], R[m])



answer = 0
for n in range(4):
    if G[n][0] == '1': answer += 2**n
print(answer)
