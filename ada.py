def ada():
    first_name = "AdA"
    last_name = "LoVeLAce"
    full_name = first_name + " " + last_name
    print (first_name.lower() + " "+ last_name.lower())
    print (first_name.title() + " " + last_name.title())
    print (first_name.upper() + " " + last_name.upper())
    print (f"\t{full_name.lower()}")
    X = "Bangladesh"
    Y = "Barbados"
    print (f"The result of {X} comes first in the dictionary than {Y} is {X<Y}.")
    print (f"The result of {Y} comes first in the dictionary than {X} is {X>Y}.")

    money = 100
    expense = 23.75
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int((vuelto - pesos)*100)

    print ("Ingresar gasto:")
    print (expense)
    print ("Dinero recibido:")
    print (money)
    print(f"\nVuelto")
    print (f"\nPesos:")
    print(vuelto)
    print("Centavos:")
    print(centavos)
