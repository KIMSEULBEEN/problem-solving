sugar = int(input())

cnt_5 = sugar // 5
while cnt_5 > 0:
    sugar_rest = sugar - cnt_5*5

    if sugar_rest % 3 == 0:
        cnt_3 = sugar_rest // 3
        break

    else: cnt_5 -= 1

if cnt_5 == 0:
    if sugar % 3 == 0:
        print(sugar // 3)

    else:
        print(-1)

else:
    print(cnt_5 + cnt_3)
