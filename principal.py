from practica_2 import funciones


def menu():
    op = int(input('ingrese la opcion que desea realizar: \n\n'
                   '[1] ejercicio 1\n'
                   '[2] ejercicio 2\n'
                   '[3] ejercicio 3\n'
                   '[4] ejercicio 4\n\n'
                   'opcion: '))

    if op == 1:
        print(funciones.mayor_10())

    elif op == 2:
        num1 = int(input('ingrese el primer numero: '))
        num2 = int(input('ingrese el segundo numero: '))
        num3 = int(input('ingrese el tercer numero: '))

        funciones.numeros(num1, num2, num3)

    elif op == 3:
        num1 = int(input('ingrese un numero: '))
        num2 = int(input('ingrese otro  numero: '))

        r = funciones.division_de_cuadrados(num1, num2)
        if r == 1:
            print('los numeros ingresados son iguales')
        else:
         print(f'el resultado de la division es: {r}')

    elif op == 4:
        g = funciones.que_temperatura_es_en_celsius()
        print(f'la temperatura pasada a grados celsius es: {g}')


menu()