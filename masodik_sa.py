import sys

f = open("be1.txt", "r")
K,N,B,L=(list(map(int, f.readline().split(" "))))
hol_volt=0
tartalyok=[]
tartalyok.append(B)
for i in range(N):
    hol,mennyit=(list(map(int, f.readline().split(" "))))
    B=B-(hol-hol_volt)/100*L+mennyit
    hol_volt=hol
    tartalyok.append(B)
print(max(tartalyok))
