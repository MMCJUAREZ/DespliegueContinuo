"""
Servicios que implementan la lógica de negocio para operaciones matemáticas.
"""
from fastapi import HTTPException

def sumar(a: float, b: float) -> float:
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b



def multiplicar(a: float, b: float) -> float:
    """
    multiplica dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la multiplicacion.
    """
    return a * b

def dividir(a: float, b: float) -> float:
    """
    divide dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la división.
    """
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b
