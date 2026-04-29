usuario = input("ingrese usuario:")
contraseña = int(input("ingrese contraseña:"))

if usuario == "admin" and  contraseña == "1234":
    print("acceso total")
elif usuario == "invitado" and contraseña == "hola":
    print("acceso ilimitado")
else:
    print("error")
    