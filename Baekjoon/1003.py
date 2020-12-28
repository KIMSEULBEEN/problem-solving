pibo_arr = [[1,0],[0,1]]

for n in range(40):
    pibo_arr.append([n1+n2 for n1,n2 in pibo_arr[-2:]])

T = int(input())
answers = []
for n in range(T):
    N = int(input())
    
    answers.append(pibo_arr[N])

   
for z,o in answers:
     print(str(z) + " " + str(o))
