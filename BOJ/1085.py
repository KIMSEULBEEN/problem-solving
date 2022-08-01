x, y, w, h = list(map(int, input().split(' ')))

num1 = abs(w - x)
num2 = abs(h - y)
num3 = x
num4 = y

print(min([num1, num2, num3, num4]))