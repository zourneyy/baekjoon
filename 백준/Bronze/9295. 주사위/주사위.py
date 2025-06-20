T = int(input())

for x in range(T) :
    a, b = map(int, input().split())
    num = a + b
    print("Case "+str(x+1)+": "+str(num))
