import re
from src.citaspsiquatra import filtrar_citas

def test_filtrar_citas_simple():
    texto = "Lunes, 1 enero 2025 10:00 horas - Hospital X"
    resultado = filtrar_citas(texto)
    assert resultado == [('Lunes', '1 enero 2025', '10:00')]

def test_filtrar_citas_multiple():
    texto = (
        "Lunes, 1 enero 2025 10:00 horas - Hospital X\n"
        "Martes, 2 enero 2025 11:00 horas - Hospital Y"
    )
    resultado = filtrar_citas(texto)
    assert resultado == [
        ('Lunes', '1 enero 2025', '10:00'),
        ('Martes', '2 enero 2025', '11:00')
    ]

def test_filtrar_citas_vacio():
    texto = "No hay citas disponibles"
    resultado = filtrar_citas(texto)
    assert resultado == []