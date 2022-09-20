import numpy as np
import sys
import matplotlib.pyplot as plt

def osszead(a,b=0):
    return a+b
print(osszead(2,4))

a_r = np.random.normal([0.05,0.1],[0.1,0.2],[10000,2])
print(a_r)
a_initial_price = np.array([[10,100]])
a_price = a_initial_price * np.exp(a_r) #így csinálunk árat az eloszásból
print(a_price)
print(a_price[:,1]) #első dimenzóból az összeset akarjuk de csak az első elemet

plt.hist(a_price[:,1], bins=100)
#plt.hist(a_price[:,1], bins=100, density=1) --> sűrűségfv.
plt.figure() #új
plt.scatter(a_price[:,1],a_price[:,0])
plt.show()

sys.exit() #ezután nem hajtja végre a programkódot
r_eff = np.array([[1,2],[3,4]])
ic = np.exp(r_eff)
ic_2y= ic**2
r_2y = np.log(ic_2y)

#print(r_2y)
#print(r_eff.shape) #a mátrix alakja


a_elso = np.array([[1,2],[2,5],[2,8]])
print(a_elso)
#atlag, osszeg, kumulalas, min, max
print(np.sum(a_elso, axis=0)) #axis --> soronként vagy oszloponként szummázza
print(np.sum(a_elso, axis=1))
print(np.mean(a_elso, axis=0))
print(np.std(a_elso, axis=0))
print(np.min(a_elso, axis=0))
print(np.max(a_elso, axis=0))
print(np.diff(a_elso, axis=0))

#centralizált tömb
c = a_elso - np.mean(a_elso)
print(c)
print(np.mean(c))

#indexing
is_pos = c > 0
print(is_pos)
d=c.copy()
d[is_pos]=d[is_pos]+100
#d[~is_pos]=d[~is_pos]+100 --> a ~ jel tagadást jelent

a_new = np.array([[2,2],[2,4],[0,4]])
print(a_new.std(axis=1))
print(a_new.std(axis=1, ddof=0)) #degree of freedom
print(a_new.std(axis=1, ddof=1)) #n-nel vagy n-1 gyel osztunk le

#random numbers
a_rnd = np.random.random((3,2))
np.random.seed(112) # mindig ugyanazt a randomszámot fogja dobni





