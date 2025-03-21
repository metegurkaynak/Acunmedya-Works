kullaniciyas = int(input("Yaşınızı giriniz:"))
def nezaman100(kullaniciyas):
    kalan = 100 - kullaniciyas
    return "Kalan yıl sayınız {}".format(kalan)
print(nezaman100(kullaniciyas))