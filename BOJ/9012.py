N = int(input())

def stryn(ParS,leftP):
    for _str in ParS:
        if _str == '(': leftP += 1
        else: 
            leftP -= 1
            if leftP < 0 : 
                return False

    if leftP == 0: return True
    else: return False


for n in range(N):
    leftP = 0
    ParS = input()

    treat = stryn(ParS,leftP)
    if treat: print('YES')
    else: print('NO')
