def mayor_10():
    num = int(input('ingrese un numero:'))

    if num > 10:
        print(f'el numero ingresado es: {num}')
    elif num < 10:
        print(f'el numero ingresado es menor a 10')
    else:
        print('el numero ingresado es igual a 10')


def numeros(var1, var2, var3):
    suma = var1 + var2

    if var3 == suma:
        print('la suma es igual al tercero')
    else:
        print('la suma es distinto al tercero')


def division_de_cuadrados(num1, num2):
    resultado = 1
    if num1 > num2:
        resultado = (num1 * num1) / (num2 * num2)
    elif num2 > num1:
        resultado = (num2 * num2) / (num1 * num1)
    else:
        resultado = 1
    return resultado


def que_temperatura_es_en_celsius():
    var1 = float(input('ingrese la temperatura a convertir en celsius'))
    c= (5 / 9) * (var1 - 32)
    return c
