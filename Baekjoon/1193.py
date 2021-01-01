N = int(input())

sum = 0

num = 0

while sum < N:
    num += 1
    sum_past = sum
    sum += num
    
if num%2 == 0:
    bm =  num - (N- sum_past) + 1
    bz = (N-sum_past)

else:
    bz =  num - (N- sum_past) + 1
    bm = (N-sum_past)
    

print(str(bz) + '/' + str(bm))
