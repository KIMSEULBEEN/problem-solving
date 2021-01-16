N = int(input())


input_arr = []
for n in range(N):
    input_arr.append(input())

cnt = 0

for n in range(N):
    num_ch_past = -1
    tmp = []
    for i in range(26):
        tmp.append(0)

    for m in range(len(input_arr[n])):
        num_ch = ord(input_arr[n][m]) - 97

        if num_ch_past != num_ch:
            tmp[num_ch] += 1

        num_ch_past = num_ch

    if max(tmp) <= 1:
        cnt += 1

print(cnt)
