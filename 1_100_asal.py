for i in range (1,101):
    asal = True
    for j in range(2,i):
        if i % j == 0:
            asal = False
            break
    if asal:
        print(i)

        