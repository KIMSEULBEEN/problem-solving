import sys
input = sys.stdin.readline

while True:
    num = input().rstrip()
    if num == '0':
        break
    else:
        idx_mid = len(num) // 2
        if idx_mid == 0:
            print('yes')
        else:
            if len(num) % 2 == 1:
                idx_s = idx_mid - 1
                idx_e = idx_mid + 1
            else:
                idx_s = idx_mid - 1
                idx_e = idx_mid
            while idx_s >= 0:
                if num[idx_s] != num[idx_e]:
                    print('no')
                    break
                else:
                    idx_s -= 1
                    idx_e += 1

                    if idx_s == -1:
                        print('yes')



