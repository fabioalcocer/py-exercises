"""
1- Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
"""

# def funcion_max(n1,n2):
#     if n1 > n2:
#         return n1
#     else:
#         return n2

# print(funcion_max(-1,5));



"""
2- Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

# def funcion_max_three(num1, num2, num3):
#   if num1 > num2 and num1 > num3:
#     return num1
#   elif num2 > num1 and num2 > num3:
#     return num2
#   else:
#     return num3

# print(funcion_max_three(10,4,2))


"""
4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

# def isVocal(char):
#     vocales = ["a", "e", "i", "o", "u"]
#     if char in vocales:
#         return True
#     else:
#         return False
        
# print(isVocal("a"))


"""
5- Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

# def sum(lista):
#     result = 0
#     for n in lista:
#         result = result + (n)
#     return(result)

# print(sum([2,10,18]));


# def mult(lista):
#     mult = 1
#     for i in lista:
#         mult *= i
#     return mult
# print(mult([2, 4, 5]))


"""
6- Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

# def invertir(cadena):
#     long = -(len(cadena)-1)
#     nuevaCadena = str()
#     for caracter in range(long, 1):
#         caracter = abs(caracter)
#         nuevaCadena += cadena[caracter]
#     return nuevaCadena

# print(invertir("Hola Mundo"))

# MI VERSION DEL PROBLEMA 6
# cadena = "Hola Mundo"
# long = len(cadena)
# for caracter in range(long -1 , -1, -1):
#     print(cadena[caracter], end = "")


"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

# def palindromos(cadena):
#     nuevaCadena = invertir(cadena)
#     if nuevaCadena == cadena:
#         return True
#     else:
#         return False
# print(palindromos("radar"))


"""
8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""
# def superposicion(lista1,lista2):
#     for elem in lista1:
#         if elem in lista2:
#             return True
#     return False
    
# print(superposicion([1,2,3],[7,1,5]))


"""
9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
# def generar_n_caracteres(caracter,n):
#     print(caracter * n)
    
#     '''    
#     string = caracter
#     for i in range(1, n):
#         string += caracter

#     print(string)
#     '''
# generar_n_caracteres('L',2)

"""
10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******
# """

# def procedimiento(lista):
#     for n in lista:
#         histograma = '*' * n
#         print(f'{histograma} \n')
# procedimiento([2,4,8])



''' Realizar una funcion llamada separar() que tome una lista de números enteros llenada aleatoramente y devuelva dos listas ordenadas. La primera lista con numeros pares, y las segunda con números impares, la cantidad de numeros para la lista es parametro de entrada. '''

# import random
# numeros = []

# def separar(lista, cantidad):
#   hacerLista(lista, cantidad)
#   pares = []
#   impares = []
#   for i in lista:
#     if i % 2 == 0:
#       pares.append(i)
#     else:
#       impares.append(i)
#   return pares, impares


# def hacerLista(lista, cantidad):
#   for i in range(cantidad):
#     lista.append(random.randint(0,100))

# pares, impares = separar(numeros, 6)
# print("pares: ", pares, "impares: ", impares)



'''Realizar un programa que permita introducir una frase e identificar si en esta frase 
se encuentran palabras reservadas de python, 
de ser así, devolver un arreglo (lista) con la o las palabras reservadas encontradas;
caso contrario dar un mensaje informando que la frase no tiene palabras reservadas. 
En el desarrollo del programa debe usar por lo menos una función.'''

import keyword
def wordsReserverd(frase):
  palabrasReservadas = keyword.kwlist
  lista = frase.split()
  encontradas = []

  for palabra in palabrasReservadas:
    for i in range(len(lista)):
      if palabra == lista[i]:
        encontradas.append(palabra)

  if len(encontradas) == 0:
    print("Ninguna palabra coincide")
  else:
    print(encontradas)

  return encontradas


frase = input("Introduzca la frase: ")
wordsReserverd(frase)

