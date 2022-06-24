# Author: Grupo 15
# Version: 1.0
# Date: 21/06/22
# Description: Repositorio de prácticas para la materia Programación del ISPC 1° Año.

def suma(a,b,c):
    return(a+b+c)

def resta(a,b):
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))    
    return(a-b)


if __name__=="__main__":
    print("Primer programa en Python !!")
    print("La suma es: ", str(suma(1,2,3)))
    print("La resta es: ", str(resta))
