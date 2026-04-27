clima = input("como esta el clima?:").lower()
#soleado,lluvioso,nevado,nublado y da una recomendacion
match clima:
    case"soleado":
        print("usa bloqueador")
    case"lluvioso":
        print("lleva paraguas")
    case"nevado":
        print("abrigate bien")
    case"nublado":
        print("lleva una chaleca porciacaso")
    case _:
         print("opcion no disponible")
       