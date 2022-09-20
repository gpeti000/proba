import sys

f = open("be1.txt", "r")
ar,N=(list(map(int, f.readline().split(" "))))
ermek=(list(map(int, f.readline().split(" "))))
ermek=sorted(ermek)

while ermek[len(ermek)-1]>ar:
    ermek.pop()
ki=[]
while ar>0:
    ar = ar - ermek[len(ermek) - 1]
    ki.append(ermek.pop())
if len(ki)>3:
    print("NEM LEHET")
else:
    print(ki)