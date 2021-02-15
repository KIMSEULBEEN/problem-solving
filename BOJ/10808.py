engArray = [0]*26

for ch in input():
    engArray[ord(ch)-97] += 1

for num in engArray:
    print(num,end=' ')
