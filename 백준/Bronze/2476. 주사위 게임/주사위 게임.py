N = 0
prize = 0
dice = []
result = []

N = int(input())

while N > 0 :
    a, b, c = map(int, input().split())

    if a==b==c :
        prize = 10000 + (a * 1000)
        
    elif a==b or a==c :
        prize = 1000 + (a * 100)

    elif b==c :
        prize = 1000 + (b * 100)

    else :
        dice = [a, b, c]
        dice.sort(reverse=True)
        prize = dice[0] * 100    

    result.append(prize)
    N -= 1

result.sort(reverse=True)
print(result[0])
