import sys

a = int(sys.stdin.readline())

for i in range(1, a+1):
    A,B = map(int, sys.stdin.readline().split())
    print("Case #" + str(i) + ":", A, "+", B, "=", A+B)