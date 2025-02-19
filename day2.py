faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(vade + 12)
print(type(vade))
print(type(faiz))
print(type(krediAdi))

print(int(vade + 12))
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
vade = vade + 12

print("Seçtiğiniz vade sonucunda ortaya çıkan vade: ", str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

isim = input("İsminizi giriniz: ")
metin = "Merhaba, {isim}".format(isim=123)
print(metin)

metin = f"Hoşgeldiniz {1+1}"
print(metin)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(krediler[0])
print(len(krediler))
print(krediler[3]) # Hata verir

dizi = ["İhtiyac Kredisi", 10, 5.2, True]

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")

krediler.pop()
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

for i in range(10):
    print("xx")
    print(i)

x = 10
for i in range(x):
    print("xx")
    print(i)
print("**************")

for i in range(5,11):
    print(i)

print("**************")
for i in range (0,51,10):
    print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
    print("**************")
    for i in range(3):
        print(krediler[i])

i = 0
while i < 10:
    print("x")
    i = i + 1
print("y")


while True:
    print("x")
    break


i=0
while i < len(krediler):
    print(krediler[i])
    i += 1
    if krediler[i] == "Konut Kredisi":
        break

fiyat = 100
indirim = 20

def calculate():
    print(100-20)

calculate()
calculate()
calculate()

def CalculateWithParams(fiyat, indirim):
    print(fiyat - indirim)

CalculateWithParams(50 , 10)
CalculateWithParams(100 , 30)

def sayHello():
    print("Hello {name}")

sayHello("Mete")
sayHello("Halit")

def calculateAndReturn(fiyat, indirim):
    return fiyat - indirim

yeniFiyat = calculateAndReturn(200 , 50)
print(yeniFiyat + 10) 

def calculatePrice(price, discount):
    print(price - discount)

def calculatePriceAndReturn(price, discount):
    return price - discount

fonk1=calculatePrice(100, 20)
fonk2=calculatePriceAndReturn(300, 100)
print("135. satır: ", fonk1)
print("136. satır: ", fonk2)
print("137. satır: ", fonk2 + 100)
print("138. satır: ", fonk1 + 100)

class Human:
    def talk(self,sentence):
        namme = "Mete"
        print(f"{name} : {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

human1 = Human()
# human1.name= "Mete"
human1.talk()
human1.talk("Merhaba")
human1.walk("Mete")

human2 = Human()
# human2.name = "Ahmet"
human2.talk("Selam","Mete")
human2.walk("Ahmet")

class Human:

def __init__(self, name):
    print("Bir human instance oluşturuldu")
    def talk(self, sentence):
        print(f"{self.name} : {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

human1 = Human("Mete")
human1.talk("Merhaba")
human1.walk()

human2 = Human("Ahmet")
human2.talk("Selam")
human2.walk()
