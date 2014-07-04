#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Algoritmo de calculo y verificacion CIF personas juridicas
# en especial para las Comunidades de Propietarios

import re

class CheckingCIF:
    """
    Esta clase define un codigo CIF.
    Tiene un unico atributo: cif
    Metodos:
        _limpiarCIF(self): limpia de caracteres extraños el atributo cif de la instancia y retorna la propia
                            instancia.
        validarCodigoCIF(self): dada una instancia devuelve True si el codigo CIF (atributo cif de la instancia
                            es un CIF valido) o False en caso contrario.
    """

    _letras = "ABCDEFGHIJKLMNPQRSVW"    # Not used yet.

    def __init__(self, un_cif):
        self.cif = un_cif
        self._limpiarCIF()

    def _limpiarCIF(self):
        self.cif = re.sub('\W', "", self.cif.upper())
        return self

    def validarCodigoCIF(self):
        if len(self.cif) != 9:
            return False
        numero = self.cif[1:10]
        pares = int(numero[1]) + int(numero[3]) + int(numero[5])
        impares = 0
        for i in range(0, 8, 2):
            j = int(numero[i]) * 2
            if j < 10:
                impares += j
            else:
                impares += j - 9
        digito = str(pares+impares)[-1]
        if int(digito) == 0:
            checkCIF = 0
        else:
            checkCIF = 10 - int(digito)
        if str(checkCIF) == self.cif[-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    entradaCodigoCIF = input('Enter the VAT number: ')
    mi_cif = CheckingCIF(entradaCodigoCIF)
    print(mi_cif.cif)
    print(mi_cif.validarCodigoCIF())