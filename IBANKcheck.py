#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Algoritmo de calculo y verificacion de CCC e IBAN para cuentas
# bancarias de España.


# Multiplicadores Digitos CCC
lista_entidad_sucursal = [4, 8, 5, 10, 9, 7, 3, 6]
lista_cuenta_cliente = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]


def digitoEntidadSucursal(entidad, sucursal):
    """Devuelve el dígito D de control de una sucursal bancaria dada.
    Para ello se le pasan el código de entidad y el código de sucursal,
    conforme a la normativa bancaria de España

    Args:
        entidad: (str), longitud 4 caracteres numéricos de 0 a 9
        sucursal: (str), longitud 4 caracteres numéricos de 0 a 9
    Returns:
        digito: (int), entero de 0 a 9

    Raises:
        nada
    Examples:
        digitoEntidadSucursal('0049', '0507')
        0
    """
    cadena = entidad + sucursal
    numeroTotal = 0
    for i in range(len(cadena)):
        numeroTotal += int(cadena[i]) * lista_entidad_sucursal[i]
    resto = numeroTotal % 11
    # if __name__ == '__main__':  print(resto)    # Para depuración
    digito = 11 - resto
    # if __name__ == '__main__':  print(digito)   # Para depuración
    if digito == 10:    # Excepciones cuando el resultado es 10 u 11
        digito = 1
    elif digito == 11:
        digito = 0
    return digito


def digitoCuenta(numeroCuenta):
    """Devuelve el dígito C de control de un numero de cuenta bancaria dado.
    Para ello se le pasan el numero de cuenta normalizado de 10 dígitos,
    conforme a la normativa bancaria de España

    Args:
        numeroCuenta: (str), longitud 10 caracteres numéricos de 0 a 9.
    Returns:
        digito: (int), entero de 0 a 9

    Raises:
        nada
    Examples:
        digitoCuenta('2190988088')
        1
    """
    numeroTotal = 0
    for i in range(len(numeroCuenta)):
        numeroTotal += int(numeroCuenta[i]) * lista_cuenta_cliente[i]
    resto = numeroTotal % 11
    # if __name__ == '__main__':  print(resto)    # Para depuración
    digito = 11 - resto
    # if __name__ == '__main__':  print(digito)   # Para depuración
    if digito == 10:    # Excepciones cuando el resultado es 10 u 11
        digito = 1
    elif digito == 11:
        digito = 0
    return digito


def getIBAN_ES(numeroCCC):
    """
    Devuelve el número de Cuenta Bancaria con formato IBAN de una
        cuenta en España, conforme a la ISO/IEC 7064 (MOD 97-10).

    Args:
        numeroCCC: (str), longitud 20 caracteres numéricos de 0 a 9.
    Returns:
        codigoIBAN: (str), longitud 24 caracteres numéricos de 0 a 9.

    Raises:
        nada
    Examples:
        getIBAN_ES('0490507012190988088')
        'ES7000490507012190988088'
    """
    spainCode = '142800'
    spainISO = 'ES'
    numeroTotal = int(''.join([numeroCCC, spainCode]))
    digitoIBAN = '{0:0>2}'.format(98 - int(numeroTotal % 97))
    codigoIBAN = ''.join([spainISO, digitoIBAN, numeroCCC])
    return codigoIBAN


if __name__ == '__main__':
    entradaEntidad = input('Introduce Código Entidad: ')
    entradaSucursal = input('Introduce Código Sucursal:')
    entradaCuenta = input('Introduce Número de Cuenta: ')
    digitoD = digitoEntidadSucursal(entradaEntidad, entradaSucursal)
    digitoC = digitoCuenta(entradaCuenta)
    print(digitoD, digitoC)
    numeroCCC = ''.join([entradaEntidad, entradaSucursal, str(digitoD),
                         str(digitoC), entradaCuenta])
    codigoIBAN = getIBAN_ES(numeroCCC)
    print(codigoIBAN)
