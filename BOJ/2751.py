import sys 
readline = lambda: sys.stdin.readline() 
N = int(readline()) 
A = [] 

for _ in range(N): 
    A.append(int(readline())) 

A.sort() 
for i in A: 
    print(i)
