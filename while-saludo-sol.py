continuar = True
while continuar:
    res = str(input("Quieres un saludo? S/N : "))
    if res == 'S' or res=='s':
        print("Hola")
    else:
        if res == 'N' or res=='n' :
            print("Ya no me quieres saludar")
            continuar = False
        else:
            print("La opción no es válida")

