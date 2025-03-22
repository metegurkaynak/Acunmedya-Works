kelimeler = []
while True:
    kelime = input("Kelime giriniz (Çıkmak için q tuşuna basın.) ")
    if kelime == "q":
        break
    kelimeler.append(kelime)
kelimeler.reverse()
print("Girilen kelimeler:")
for kelime in kelimeler:
    print(kelime)