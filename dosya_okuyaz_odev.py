def dosyaya_yaz(dosya_adi,metin):
    with open(dosya_adi , "w", encoding="utf-8") as dosya:
        dosya.write(metin)
    print(f"{dosya_adi} adlı dosyaya yazıldı.")

def dosyayi_oku(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
        print(f"{dosya_adi} adlı dosyanın içeriği:\n {icerik}")

def bes_satir_kaydet(dosya_adi):
    with open(dosya_adi,"w", encoding="utf-8") as dosya:
        for i in range(1,6):
            satir = input(f"{i}. satırı girin: ")
            dosya.write(satir + "\n")
    print(f"{dosya_adi} adlı dosya kaydedildi.")

def satir_satir_oku(dosya_adi):
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        print(f"{dosya_adi} adlı dosyanın satır içeriği:")
        for satir in dosya:
            print(satir.strip())

if __name__ == "__main__":
    dosya_adi1 = "metin.txt"
    metin = input("Dosyaya yazılacak metni girin: ")
    dosyaya_yaz(dosya_adi1, metin)
    dosyayi_oku(dosya_adi1)

    dosya_adi2 = "satirlar.txt"
    bes_satir_kaydet(dosya_adi2)
    satir_satir_oku(dosya_adi2)

   