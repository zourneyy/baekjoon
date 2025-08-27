N = 0

N = int(input())
maxstar = 2 * N - 1

for i in range(1, N+1):
    star = 2 * i - 1
    blank = (maxstar - star) // 2
    print(" " * blank, end='')
    print("*" * star)

for i in range(N-1, 0, -1):
    star = 2 * i - 1
    blank = (maxstar - star) // 2
    print(" " * blank, end='')
    print("*" * star)
