input = input()

leni = len(input)

mok = int(leni/10)
na = int(leni%10)
idx = 0

for n in range(mok):
    for k in range(10):
        print(input[10*n+k],end='')
    print()

for k in range(na):
    print(input[10*mok+k],end='')

print()
