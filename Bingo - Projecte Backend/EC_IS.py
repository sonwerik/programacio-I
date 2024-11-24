#Codigo creado por Èrik Calvo e Iván Salvador.

import random
import sys

numeros_salidos = set()
carton = []


def crear_carton(columna, fila, num_inicio, num_final):
    global carton

    for i in range(fila):
        numeros_fila = random.sample(range(num_inicio, num_final), columna)
        carton.append(numeros_fila)

    print('\033[92m{}\033[0m'.format('\nTu carton ha sido creado correctamente'))
    print('Selecciona la segunda opcion para verlo.\n')


def ver_carton():
    print('\r', *carton, '\r', sep="\n")


def dar_bola(num_inicio, num_final):
    global numeros_salidos

    bola = random.randint(num_inicio, num_final)
    while bola in numeros_salidos:
        bola = random.randint(num_inicio, num_final)

    numeros_salidos.add(bola)
    print('\nBola numero: ', bola)

    bola_encontrada = False

    for fila in carton:
        if bola in fila:
            sustituir_indice = fila.index(bola)
            fila[sustituir_indice] = 'X'
            bola_encontrada = True
            print('\033[92m{}\033[0m'.format("¡Encontraste una bola!\n"))

    if not bola_encontrada:
        print("Esa bola no está en tu cartón.\n")
    comprobar_bingo()


def comprobar_bingo():
    for fila in carton:
        for num in fila:
            if num != 'X':
                return False
    print('\033[92m{}\033[0m'.format("¡Bingo!\n"))
    sys.exit()


def ver_numeros_salidos():
    print('Estos son los números que ya han salido.\n')
    print(numeros_salidos, end=', ')
    print('\n')

def menu_inicio():
    global carton

    print('Este pequeño juego ha sido creado por Ivan Salvador y Erik Calvo.')
    print('¡Bienvenidos al menú principal!\n')

    while True:
        print('0. Salir')
        print('1. Crear carton')
        print('2. Ver carton')
        print('3. Pedir bola')
        print('4. Ver números salidos')

        opcion = input('Elige una opción: ')

        if opcion == '0':
            break

        elif opcion == '1':
            if not carton:
                fila = int(input("¿Cuántas filas debe tener el cartón?: "))
                columna = int(input("¿Cuántas columnas debe tener el cartón?: "))
                num_inicio = int(input("¿Número de inicio que debe tener el número?: "))
                num_final = int(input("¿Número de final que debe tener el número?: "))
                crear_carton(columna, fila, num_inicio, num_final)

            else:
                print("\nYa tienes un cartón\n")

        elif opcion == '2':
            if not carton:
                print("\nPrimero tienes que crear un cartón\n")
            else:
                ver_carton()

        elif opcion == '3':
            if not carton:
                print("\nPrimero tienes que crear un cartón\n")
            else:
                dar_bola(num_inicio, num_final)

        elif opcion == '4':
            if not carton:
                print("\nPrimero tienes que crear un cartón\n")
            else:
                ver_numeros_salidos()


menu_inicio()