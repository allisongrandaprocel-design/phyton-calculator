#CALCULADORA EN PHYTON 
print("Calculadora en Phyton")
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
#Phyton no ejecuta nada aqui, solamente ejecuta texto.
print("Seleccione una operacion: ")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACION")
print("4. DIVISION")
opcion = input("Opcion: " )
if opcion == "1":
    print("RESULTADO: ", a + b)
elif opcion == "2":
        print("RESULTADO", a - b)    
elif opcion == "3":
    print("RESULTADO: ", a * b)
elif opcion == "4":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("No se puede dividir para 0: ")
else:
    print("Opcion invalida: ")    


