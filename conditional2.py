yas = int(input("Yaşınızı giriniz:"))
if yas >= 60:
    print("Yaşlısınız.")
elif 20 <= yas <= 60:
    print("Yetişkinsiniz.")
elif 13 <= yas <= 19:
    print("Gençsiniz.")
elif 0 <= yas <= 12:
    print("Çocuksunuz.")    