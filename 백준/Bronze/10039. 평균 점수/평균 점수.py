score = []
for i in range(5):
    num = int(input())
    if num < 40 :
        num = 40
        score.append(num)
    else :
        score.append(num)

    
avg = sum(score) // 5
print(avg)
