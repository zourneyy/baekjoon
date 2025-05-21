total = 0
minute = 0
sec = 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())

total = a + b + c + d
minute = total // 60
sec = total % 60

print(minute)
print(sec)