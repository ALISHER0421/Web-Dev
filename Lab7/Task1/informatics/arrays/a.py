n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if i % 2 == 0:
        print(a[i], end=' ')
