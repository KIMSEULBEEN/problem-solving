a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)


ans1 = (a+b)%c

ans2 = (a%c + b%c)%c

ans3 = (a*b)%c

ans4 = ((a%c)*(b%c))%c

print(ans1)
print(ans2)
print(ans3)
print(ans4)



