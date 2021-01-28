N = int(input())



for num in range(N):
    rnum,input_str = input().split()

    rnum = int(rnum)

    tmp = ''

    len_str = len(input_str)
    for n in range(len_str):
        for m in range(rnum):
            tmp += input_str[n]


    print(tmp)
