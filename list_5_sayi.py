list = []
for i in range(5):
    sayi = int(input("Sayı giriniz: "))
    list.append(sayi)
print("Girilen sayılar: ", list)
print("En büyük sayı: ", max(list))
print("En küçük sayı: ", min(list))
print("Ortalama: ", sum(list)/len(list))
