def ImprimirPantalla():
    print("OPCIONES:\n", "1- Sumar\n", "2- Salir\n")

def SumaNumeros(num1,num2):
    return (num1+num2)

opcion=0




opcion=0


while (opcion!=2):
    ImprimirPantalla()
    opcion=(int)(input("Dime la opción que quieres elegir\n"))
    if (opcion==1):
        num1=0
        num2=0
        num1=(int)(input("Dime el primer número\n"))
        num2=(int)(input("Dime el segundo número\n"))
        print ("La suma es",SumaNumeros(num1,num2))
