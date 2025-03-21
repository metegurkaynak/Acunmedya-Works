sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
islem = input("İşlem türünü giriniz (+,-,*,/): ")
def hesapla(sayi1,sayi2,islem):
    if islem == "+":
        return sayi1 + sayi2    
    elif islem == "-":
        return sayi1 - sayi2   
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
        return sayi1 / sayi2
    else:
        return "Hatalı işlem türü girdiniz."
print(hesapla(sayi1,sayi2,islem))
