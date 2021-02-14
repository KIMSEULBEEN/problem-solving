score_arr = []


for n in range(5):
    tmp = int(input())
    if tmp<40:
        tmp = 40

    score_arr.append(tmp)


avg = int(sum(score_arr)/len(score_arr))

print(avg)
