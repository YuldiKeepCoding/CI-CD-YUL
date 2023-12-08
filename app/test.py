"""
Este es un módulo de prueba para el proyecto.
Incluye funciones de prueba para probar la funcionalidad del código.
"""
from main import Calculadora

def test_add():
    """
    Pruebas unitarias para el método add de la clase Calculadora.
    """
    assert Calculadora().add(1, 2) == 3.0
    assert Calculadora().add(1.0, 2.0) == 3.0
    assert Calculadora().add(0, 2.0) == 2.0
    assert Calculadora().add(2.0, 0) == 2.0
    assert Calculadora().add(-4, 2.0) == -2.0

def test_subtract():
    """
    Pruebas unitarias para el método subtract de la clase Calculadora.
    """
    assert Calculadora().subtract(1, 2) == -1.0
    assert Calculadora().subtract(2, 1) == 1.0
    assert Calculadora().subtract(1.0, 2.0) == -1.0
    assert Calculadora().subtract(0, 2.0) == -2.0
    assert Calculadora().subtract(2.0, 0.0) == 2.0
    assert Calculadora().subtract(-4, 2.0) == -6.0

def test_multiply():
    """
    Pruebas unitarias para el método multiply de la clase Calculadora.
    """
    assert Calculadora().multiply(1, 2) == 2.0
    assert Calculadora().multiply(1.0, 2.0) == 2.0
    assert Calculadora().multiply(0, 2.0) == 0.0
    assert Calculadora().multiply(2.0, 0.0) == 0.0
    assert Calculadora().multiply(-4, 2.0) == -8.0

def test_divide():
    """
    Pruebas unitarias para el método divide de la clase Calculadora.
    """
    # assert Calculadora().divide(1, 2) == 0.5
    assert Calculadora().divide(1.0, 2.0) == 0.5
    assert Calculadora().divide(0, 2.0) == 0
    assert Calculadora().divide(-4, 2.0) == -2.0
    # assert Calculadora().divide(2.0, 0.0) == 'Cannot divide by 0'
