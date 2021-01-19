import sys


count = []
C = []
for n in range(8001):
    count.append(0)


readline = lambda: sys.stdin.readline() 
N = int(readline()) 

for n in range(N):
    num = int(readline())
    count[num + 4000] += 1

for n in range(8001):
    for m in range(count[n]):
        # print(n-4000)
        C.append(n-4000)


avg = round(sum(C)/len(C))


print(avg)
print(C[int(len(C)/2)])

max_i_1 = count.index(max(count))
temp = count[max_i_1]
count[max_i_1] = 0
max_i_2 = count.index(max(count))



if temp == count[max_i_2]:
    print(max_i_2 - 4000)
else:
    print(max_i_1 - 4000)


print(C[len(C)-1]-C[0])
