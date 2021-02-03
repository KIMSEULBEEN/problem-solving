def sumarr(arr):
    len_arr = len(arr)

    sum_arr = []
    sum = 0
    for n in range(len_arr):
        sum += arr[n]
        sum_arr.append(sum)

    return sum_arr

arr = []

arr_ori = []
for n in range(1,15):
    arr_ori.append(n)


repeat = int(input())


for r in range(repeat):
    a = int(input())
    b = int(input())

    arr = arr_ori
    for n in range(a):
        arr = sumarr(arr)


    print(arr[b-1])
