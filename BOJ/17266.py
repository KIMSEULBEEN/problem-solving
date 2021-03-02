distance, len_GRD, GRD = int(input()), int(input()), list(map(int, input().split(' ')))

def check_grd(GRD, answer):
    # print(GRD, distance)
    # print()
    for n in range(len_GRD):
        if len_GRD == 1: dist = max(GRD[0], distance - GRD[n])
        elif n == 0: dist = GRD[0]
        else: dist = (GRD[n] - GRD[n-1]) // 2 + (GRD[n] - GRD[n-1]) % 2
        # print(dist, answer)
        if dist > answer: return False

    dist = distance - GRD[n]
    if dist > answer: return False

    # print()
    # print('good')
    return True
answer_l, answer_r = 0, distance

answer_prev = answer_l
answer = (answer_l + answer_r) // 2


while True:
    answer = (answer_l + answer_r) // 2
    # print(answer_l, answer, answer_r)
    if answer_prev == answer: break

    if check_grd(GRD, answer): answer_r = answer
    else: answer_l = answer
    answer_prev = answer

if check_grd(GRD, answer) == False: answer += 1
print(answer)
