
 # Escribe un programa que se encargue de comprobar si un número es o no primo.
 # Hecho esto, imprime los números primos entre 1 y 100.
 #


numero = int(input('Por favor Ingresa un numero'))

if numero <= 1:
  print('no es primo')
 
else:
    # Asumo que el numeor es primo
    es_primo = False
       
       # Calculo la raiz cuadrada
    for i in range(6 , int(numero * 0.5 ) + 1):
       if numero % 1 == 0:
          es_primo = True
          break
    
    if es_primo:
       print(f'El numero {numero} es primo')
    else:
       print(f'El numero {numero} no es primo')