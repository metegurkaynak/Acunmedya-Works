kelime = str(input("Kelimeyi giriniz: "))
def palindrom(kelime):
    if kelime == kelime[::-1]:
        return "Bu kelime bir palindromdur."
    else:
        return "Bu kelime bir palindrom değildir."
print(palindrom(kelime))