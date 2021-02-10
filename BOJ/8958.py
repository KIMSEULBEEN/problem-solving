N = int(input())



for i in range(N):

    str_a = input()
    len_a = len(str_a)

    score = 1
    sum = 0
    for n in range(len_a):
        if str_a[n] == 'O':
            sum += score
            score += 1
            

        else:
            score = 1


    print(sum)

