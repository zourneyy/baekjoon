time = 3
ans = []

while time > 0:
    N = 0
    S = 0
    a = 0
    
    N = int(input())
    for i in range(N):
        a = int(input())
        S += a

    if S == 0:
        ans.append("0")    
    elif S >= 0:
        ans.append("+")    
    elif S <= 0:
        ans.append("-")

    time = time - 1

for j in range(len(ans)):
    print(ans[j])
