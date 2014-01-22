IBAN-checking
=============

SPANISH:
--------
Módulo/Librería para obtener y validar cuentas bancarias IBAN (International Bank Account Number) de España.  La entrada en vigor en la Unión Europea del proyecto SEPA (Single Euro Payments Area, http://www.sepaesp.es/) el próximo día 1 de Febrero de 2014, hace obligatoria la utilización del nuevo número de cuenta bancaria con formato IBAN.

El formato del IBAN está establecido por la norma ISO 13616-1:
    Financial services - International bank account number (IBAN) - Part 1:Structure of the IBAN
    
A su vez, se hace uso de la norma ISO 3166-1-alpha-2 para el código de país (España -> ES) y de la norma ISO/IEC 7064 (MOD97-10) para el cálculo de los dígitos de control.

Hasta ahora en España se venía usando el CCC establecido en el Cuaderno 37 de la AEB (Asociación Española de Banca, http://www.aebanca.es/)

Estructura del CCC (Código Cuenta Cliente):

Entidad/Oficina/D.C./Número de Cuenta = EEEE OOOO DD NNNNNNNNNN
- EEEE= Código Entidad.  Asignado por el Banco de España.
- OOOO= Código Oficina.
- DD= Dígitos de Control, 2: (el primero, dígito 'D', chequea los códigos de Entidad y Oficina; el segundo, dígito 'C' chequea el número de cuenta)
- NNNNNNNNNN= Numero de cuenta bancaria.

Todos son dígitos numéricos del 0 al 9.

Estructura del IBAN (International Bank Account Number) en España: ESDD EEEE OOOO DDNN NNNN NNNN
* ES= Código ISO del país, en este caso España
* DD= Dígitos de Control de toda la CCC
* EEEE= Código Entidad.  Asignado por el Banco de España.
* OOOO= Código Oficina.
* DD= Dígitos de Control, 2.

Como se puede ver se añade el literal 'ES', que es el código ISO de España y a continuación otros 2 dígitos de control, que en su verión impresa se agruparán de cuatro en cuatro caracteres separados por un espacio en blanco.

De momento sólo hay definidas 3 funciones:
- getDigitoD('EEEE', 'OOOO') -> int
    digito de 0 a 9
- getDigitoC('NNNNNNNNNN') -> int
    digito de 0 a 9
- getIBAN_ES('EEEEOOOODDNNNNNNNNNN) -> str
    cadena de texto de 24 caracteres en formato digital (sin espacios)


<B>TODO:</B>
<OL>
<LI>Función que devuelva el CCC completo pasando EEEE, OOOO y NNNNNNNNN
<li>Función que devuelva el IBAN completo pasando EEEE, OOOO y NNNNNNNNN
<li>Función que verifique si CCC es correcto, devolviendo Booleano.
<li>Función que verifique si IBAN es correcto, devolViendo Booleano.
<li>Excepciones de error?
<li>Clase?
</OL>

Madrid, Salvaj€, 22/01/2014
Licencia: GPLv2 (GNU General Public License version 2)
Código Fuente: https://github.com/SalvaJ/IBAN-checking/



ENGLISH:
--------
Coming soon...  ;-)
