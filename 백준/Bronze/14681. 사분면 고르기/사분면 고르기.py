x = int(input())
y = int(input())
Q = 0

if x > 0 :
    xx = 1 #양수
else :
    xx = 0 #음수

if y > 0 :
    yy = 1 #양수
else :
    yy = 0 #음수
    
if xx == 1 and yy == 1 :
    Q = 1
elif xx == 0 and yy == 1:
    Q = 2
elif xx == 0 and yy == 0 :
    Q = 3
else :
    Q = 4
    
print(Q)