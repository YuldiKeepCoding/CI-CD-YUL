"""
Este script define una calculadora simple y muestra un arte ASCII de bienvenida.
La calculadora tiene operaciones de suma, resta, multiplicación y división.
"""

print('''
'    ####      ##    ####    ####  #### ###  ####      ##    ######    ####   ######      ##'
'   ##  ##     ##     ##    ##  ##  ##  ##    ##       ##     ##  ##  ##  ##   ##  #      ##'
'  ###        ###     ##   ###      ##  ##    ##      ###     ##  ## ###  ##   ## ##     ###'
'  ##        #  ##   ##    ##      ##  ##    ##      #  ##   ##   ## ##   ##   ####     #  ##'
'  ##        #####   ##    ##      ##  ##    ##      #####   ##  ### ##  ###  ## ##     #####'
'  ##   #   #   ##   ##  # ##   #  ##  ##    ##  #  #   ##   ##  ##  ##  ##   ##  ##   #   ##'
'   ####   ### #### ######  ####    ####    ###### ### #### ######    ####   #### ### ### ####'


 _____________________
|  _________________  |
| |   Calculadora   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |   
|_____________________|

''')

class Calculadora:
    """
    Clase que implementa una calculadora con operaciones básicas.

    Attributes:
        None

    Methods:
        add(num1, num2): Realiza la operación de suma.
        subtract(num1, num2): Realiza la operación de resta.
        multiply(num1, num2): Realiza la operación de multiplicación.
        divide(num1, num2): Realiza la operación de división.

    Example:
        calc = Calculadora()
        resultado_suma = calc.add(2, 3)  # Devuelve 5
        resultado_resta = calc.subtract(5, 2)  # Devuelve 3
        resultado_multiplicacion = calc.multiply(4, 2)  # Devuelve 8
        resultado_division = calc.divide(8, 4)  # Devuelve 2.0
    """

    def add(self, num1, num2):
        """
        Realiza la operación de suma.

        Args:
            num1 (int): Primer número.
            num2 (int): Segundo número.

        Returns:
            int: Resultado de la suma.
        """
        return num1 + num2

    def subtract(self, num1, num2):
        """
        Realiza la operación de resta.

        Args:
            num1 (int): Número del que se resta.
            num2 (int): Número que se resta.

        Returns:
            int: Resultado de la resta.
        """
        return num1 - num2

    def multiply(self, num1, num2):
        """
        Realiza la operación de multiplicación.

        Args:
            num1 (int): Primer número.
            num2 (int): Segundo número.

        Returns:
            int: Resultado de la multiplicación.
        """
        return num1 * num2

    def divide(self, num1, num2):
        """
        Realiza la operación de división.

        Args:
            num1 (int): Número dividendo.
            num2 (int): Número divisor.

        Returns:
            float or str: Resultado de la división o mensaje de error si el divisor es 0.
        """
        if num2 == 0:
            return 'Cannot divide by 0'
        return num1 * 1.0 / num2
