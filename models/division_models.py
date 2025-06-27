"""
Modelos de solicitud para la API de calculadora.
"""
from pydantic import BaseModel


class DivisionRequest(BaseModel):
    """
    Modelo de datos para la operación de division.

    Attributes:
        a (float): Primer número.
        b (float): Segundo número.
    """
    a: float
    b: float
