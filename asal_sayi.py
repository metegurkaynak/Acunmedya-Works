def asal_mi(sayi):
    if sayi == 1:
        return f"{sayi} asal sayı değildir."
    elif sayi == 2:
        return f"{sayi} asal sayıdır."
    elif sayi <= 0:
        return f"{sayi} ifadesi için asallıktan bahsedilemez."
    else:
        for i in range(3, sayi):  
            if sayi % i == 0:
                return f"{sayi} asal sayı değildir."
        return f"{sayi} asal sayıdır." 

sayi = int(input("Bir değer giriniz: "))
print(asal_mi(sayi))