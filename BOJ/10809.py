str_in = input()

len_str = len(str_in)


alnum = 26
tmp = []

al = 97 # 'a'
for n in range(alnum):
    cnt = 0
    for m in range(len_str):
        if str_in[m] == chr(al):
            tmp.append(m)
            al += 1
            cnt = 1
            break

    if cnt == 0:
        tmp.append(-1)
        al += 1
        



for n in range(len(tmp)):
    print(tmp[n],end= ' ')

print()
