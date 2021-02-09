def d(n):
    n_1 = int(n%10)
    n_10 = int(int(n%100)/10)
    n_100 = int(int(n%1000)/100)
    n_1000 = int(n/1000)

    return n + n_1 + n_10 + n_100 + n_1000


num_li = 10000
numarr = list(range(num_li+1))

for n in range(1,num_li):
    num_d = n

    while num_d < num_li:
        num_d = d(num_d)
        if num_d <= num_li:
            numarr[num_d] = -1


for n in range(1,num_li+1):
    if numarr[n] != -1:
        print(numarr[n])





