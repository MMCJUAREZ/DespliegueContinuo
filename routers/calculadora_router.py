"""
Router de operaciones matemáticas para la API de calculadora.
"""

from fastapi import APIRouter
from models.request_models import SumaRequest
from models.multiplicacion_models import MultiplicacionRequest
from models.division_models import DivisionRequest
from services.operaciones_service import sumar
from services.operaciones_service import multiplicar
from services.operaciones_service import dividir

router = APIRouter()

@router.post("/suma")
def ruta_suma(datos: SumaRequest):
    """
    Calcula la suma de dos números.

    Args:
        datos (SumaRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la suma.
    """

    resultado = sumar(datos.a, datos.b)
    return {"resultado": resultado}



@router.post("/multiplicacion")
def ruta_multiplicacion(datos: MultiplicacionRequest):
    """
    Calcula la multiplicacion de dos números.

    Args:
        datos (MultiplicacionRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la multiplicacion.
    """

    resultado = multiplicar(datos.a, datos.b)
    return {"resultado": resultado}

@router.post("/division")
def ruta_division(datos: DivisionRequest):
    """
    Calcula la division de dos números.

    Args:
        datos (DivisionRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la division.
    """

    resultado = dividir(datos.a, datos.b)
    return {"resultado": resultado}
