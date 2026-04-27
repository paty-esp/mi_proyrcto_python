edad = int(input("ingrese la edad:"))

if edad <12:
    print("niño")
elif edad >=13 and edad <=17:
    print("adolecente")
elif edad >=18 and edad <=64:
    print("adulto")
elif edad >=65:
    print("adulto mayor")
else:
    print("edad imposible") 