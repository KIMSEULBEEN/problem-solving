N = int(input())

array = []
for _ in range(N): array.append(int(input()))
print(*sorted(array))
