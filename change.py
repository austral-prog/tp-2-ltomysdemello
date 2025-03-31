def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int((vuelto - pesos)*100)

    print ("Ingresar gasto:")
    print (expense)
    print ("Dinero recibido")
    print (money)
    print(f"\nVuelto")
    print (f"\nPesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
