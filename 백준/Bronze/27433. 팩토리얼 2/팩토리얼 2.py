N = int(input())
answer = N

if N == 0 :
    answer = 1
    
else :
    for i in range(1, N) :
        if i <= 0 :
           break
        answer = answer * i
        
print(answer)
