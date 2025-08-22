people = 0

out1, in1 = map(int, input().split())
out2, in2 = map(int, input().split())
out3, in3 = map(int, input().split())
out4, in4 = map(int, input().split())

p1 = people - out1 + in1
p2 = p1 - out2 + in2
p3 = p2 - out3 + in3
p4 = p3 - out4 + in4

list = [p1, p2, p3, p4]

print(max(list))
