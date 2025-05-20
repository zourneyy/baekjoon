N = int(input())
a = list(map(int, input().split()))
v = int(input())

find = []

for i in a :
    if i == v :
        find.append(i)

print(len(find))
