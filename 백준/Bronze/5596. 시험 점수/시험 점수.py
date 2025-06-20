mink = []
mans = []

mink = list(map(int, input().split()))
mans = list(map(int, input().split()))

S = sum(mink)
T = sum(mans)

if S > T :
    print(S)

elif S < T :
    print(T)

else :
    print(S)
