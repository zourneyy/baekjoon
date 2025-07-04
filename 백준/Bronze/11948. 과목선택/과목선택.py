list1 = []
select = []
total = 0

A = int(input())
B = int(input())
C = int(input())
D = int(input())

E = int(input())
F = int(input())

list1 = [A, B, C, D]
list1.sort(reverse=True)

select = list1[0:3]

if E > F:
    select.append(E)
elif F > E:
    select.append(F)
elif E == F:
    select.append(E)

total = sum(select)
print(total)
