def hesap_makinesi(sayi1,sayi2,islem):
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "-":
        return sayi1 - sayi2
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            return "Bir sayı sıfıra bölünemez."
        else:
            return sayi1 / sayi2
    else:
        return "Hatalı girdi!"
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
islem = input("Yandaki işlemlerden birini seçiniz (+,-,*,/): ")
print(hesap_makinesi(sayi1,sayi2,islem))        