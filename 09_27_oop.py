import numpy as np

class Auto(): #csinálunk sbalonokat
#az str-nek mondjuk ugyanúgy van egy ilyen class-a, ahol definiálva van a split
    negy_kereke_van = True #a sablonnak önmagában csak ezkeet az értékeket adtuk
    szamlalo = 0

    def __init__(self, szin, evjarat, futott_km, tipus): #self-fel inicializálunk, az init egy obstruktor
        self.szin = szin
        self.evjarat = evjarat
        Auto.szamlalo += 1
        self.futott_km = futott_km
        self.tipus = tipus

    def kiir_szin(self):
        print(self.szin)

    def fut(self, ut):
        self.futott_km += ut

    def __str__(self): #igy tudjuk elérni, hogy szépen legyen kiirva
        return "[Auto] szin: " + self.szin + "; evjarat: "+ str(self.evjarat)+ ";"

    def __add__(self, other):
        return self.futott_km + other.futott_km

auto_1 = Auto("Fekete", 2020, 0, "Kamion") #ez pl egy objektum
auto_2 = Auto("Piros", 2017, 100, "Autó")

auto_1.fut(1000)

print(auto_1)
print(auto_2.futott_km)
print(auto_1 + auto_2)

#print(auto_1.szin)
#auto_1.kiir_szin()
#ez a kettő ugyanaz

#print(auto_2.evjarat)
#print(Auto.negy_kereke_van)

#-----------------------------------------------

class RandomBag:
    def __init__(self):
        self.content = []


    def __str__(self):
        return "[RandomBag] :" + str(self.content)
    """
    def __add__(self, other):
        tmp = []
        for item in self.content:
            tmp.append(item)

        for item in other.content:
            tmp.append(item)
        return tmp
    """
    def __add__(self, other):
        return self.content + other.content


    def put(self, object):
        self.content.append(object)

    def pop(self):
        if len(self.content) > 0:
            index = np.random.randint(0, len(self.content))
            item = self.content[index]
            del self.content[index]
            return item
        else:
            return "Üres a táska"

    def size(self):
        return len(self.content)

bag = RandomBag()
bag.put("Alma")
print(bag.size())
print(bag)

print(bag.pop())
print(bag.pop())

for i in range(1,11):
    bag.put(i)

while bag.size() > 0:
    print(bag.pop())