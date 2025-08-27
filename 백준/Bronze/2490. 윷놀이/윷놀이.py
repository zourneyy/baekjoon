throw = 0
result = 0
count = 3

while count > 0:
    throw = list(map(int, input().split()))
    result = sum(throw)

    if result == 1 :
        print("C")

    elif result == 2 :
        print("B")

    elif result == 3 :
        print("A")

    elif result == 4 :
        print("E")

    elif result == 0 :
        print("D")

    count -= 1
