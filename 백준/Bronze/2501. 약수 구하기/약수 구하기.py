N = 0
K = 0
num = []
ans = 0

N, K = map(int, input().split())

for i in range(1, N+1):
    if N % i == 0:
        num.append(i)

num.sort()

if K > len(num):
    print("0")
else :
    print(num[K-1])