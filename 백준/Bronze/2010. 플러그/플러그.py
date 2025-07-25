import sys
input = sys.stdin.readline

N = int(input())
plug = 0

for i in range(N):
    plug += int(input())
    
com = plug - (N - 1)
print(com)
