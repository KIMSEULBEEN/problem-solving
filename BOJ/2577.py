num_arr = [0,0,0, 0,0,0, 0,0,0, 0]

A = int(input())
B = int(input())
C = int(input())

num = A*B*C
num_str = str(num)
num_len = len(num_str)

for n in range(num_len):
    n_tmp = int(num_str[n])
    num_arr[n_tmp] += 1


for n in range(10):
    print(num_arr[n])

