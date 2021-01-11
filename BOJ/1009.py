na_arr = [[0,0,0,0],[1,1,1,1]]

for n in range(2,10):
    na = [n]
    for m in range(3): na += [int(str(na[-1]*n)[-1])]
    na_arr.append(na)


    


N = int(input())

answers = []
for n in range(N):
    a,b = input().split(" ")
    a,b = int(a[-1]),int(b)
    
    answer = na_arr[a][b%4-1]
    if answer == 0: answers.append(10)
    else: answers.append(answer)

for answer in answers: print(answer)
