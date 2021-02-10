alpha = []
for n in range(26):
    alpha.append(chr(65+n))

dial_arr = []

dial_arr.append('') # 0  
dial_arr.append('') # 1

dial_arr.append(alpha[0:3]) # 2
dial_arr.append(alpha[3:6]) # 3
dial_arr.append(alpha[6:9]) # 4

dial_arr.append(alpha[9:12]) # 5
dial_arr.append(alpha[12:15]) # 6
dial_arr.append(alpha[15:19]) # 7

dial_arr.append(alpha[19:22]) # 8
dial_arr.append(alpha[22:26]) # 9



num_str = ''

input_str = input()
len_str = len(input_str)

for n in range(len_str):
    for m in range(10):
        if input_str[n] in dial_arr[m]:
            num_str += str(m)


sum = 0
for n in range(len_str):
    sum += int(num_str[n]) + 1


print(sum)
