a, b, c = map(int, input().split())
prize = 0
num = []
big = 0

if a == b and b == c and a == c :
    prize = 10000 + (a * 1000)
elif a == b or a == c :
    prize = 1000 + (a * 100)
elif b == c :
    prize = 1000 + (b * 100)
else :
    num = [a, b, c]
    num.sort()
    big = num[-1]
    prize = big * 100

print(prize)
