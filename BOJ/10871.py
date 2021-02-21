N,X = input().split()

N = int(N)
X = int(X)

N_array = input()
N_array = N_array.split(' ')
N_array = list(map(int,N_array))



for n in range(N):
    if N_array[n] < X:
        print(N_array[n],end=' ')
print()
