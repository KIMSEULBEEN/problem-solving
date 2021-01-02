N = input()
len_N = len(N)

N = N.replace('9','6')



num_arr = []
for n in range(10):
    num_arr.append(0)


for n in range(len_N):
    num_arr[int(N[n])] += 1


num_arr[6] = int(num_arr[6]/2) + num_arr[6]%2


print(max(num_arr))
