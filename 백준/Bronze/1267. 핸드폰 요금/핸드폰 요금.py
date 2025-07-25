N = 0
time = []
Y = 0
M = 0

N = int(input())
time = list(map(int, input().split()))

# Y 영식
for i in range(N):
    if time[i] < 30:
        rate = 10
        Y += rate
    else:
        rate = (time[i] // 30) * 10
        Y += rate
        if (time[i] % 29) > 0:
            Y += 10

# M 민식
for i in range(N):
    if time[i] < 60:
        rate = 15
        M += rate
    else:
        rate = (time[i] // 60) * 15
        M += rate
        if (time[i] % 59) > 0:
            M += 15

if Y > M:
    print("M", M)

elif Y < M:
    print("Y", Y)

else:
    print("Y", "M", Y)
