sayi1 = int(input("Faktoriyeli alınacak sayıyı giriniz: "))
faktoriyel = 1
for i in range(1,sayi1+1):
    faktoriyel *= i
print("Girilen sayının faktoriyeli: ",faktoriyel)