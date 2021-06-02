'''
Realiza un programa que pida al usuario cuantos números quiere introducir. 
Luego lee todos los números que se han introducido y se realiza una operación de media aritmética
Instrucciones
Para solucionar este problema, se requiere que el usuario ingrese una cantidad limitada de números por consola. 
El programa debe solicitar la cantidad de números a ingresar. Con los números ingresados debe realizar el calculo de la media. 
Este calculo es la suma de todos los números dividido por el total de números sumados. 
Ejemplo, se ingresan los números 1,2,4,5, el calculo es 1+2+4+5/4.
'''
cantidad = int(input("Ingrese la cantidad de números a los que les va a calcular la media: "))
num = []

for n in range(cantidad):
    n = (int(input("No.")))
    num.append(n) #Agregue n a a lista num

media = sum(num)/cantidad # función sum sirve para sumar elementos de una lista
print("La media de los números", num, "es: ", media)
