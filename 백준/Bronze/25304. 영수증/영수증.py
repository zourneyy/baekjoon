price = 0
total = 0

X = int(input())
N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    price = a * b
    total += price

if X == total:
    print("Yes")
else:
    print("No")
