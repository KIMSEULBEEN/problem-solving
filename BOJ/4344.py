num_cl = int(input())


score_cl = []
avg_cl = []
for n in range(num_cl):
    score_cl.append(input())
    score_cl[n] = score_cl[n].split(' ')
    score_cl[n] = list(map(int,score_cl[n]))
    del(score_cl[n][0])
    score_cl[n] = sorted(score_cl[n])

    len_scn = int(len(score_cl[n]))
    avg_score = sum(score_cl[n])/len_scn
    
    num_avgabove = 0
    for m in range(len_scn):
        if score_cl[n][m] > avg_score:
            num_avgabove += 1
    avg_cl.append((num_avgabove/len_scn) * 100)


for n in range(num_cl):
    print('%.3f'%avg_cl[n] + '%')

