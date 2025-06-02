# Citas Psiquiatría

Este proyecto tiene como objetivo obtener citas disponibles en centros de salud para consultas de psiquiatría. Utiliza solicitudes HTTP para interactuar con un servicio web y extraer información relevante sobre las citas.

## Estructura del Proyecto

- `src/citaspsiquiatria.py`: Contiene la funcionalidad principal del programa, incluyendo las funciones `obtener_citas` y `filtrar_citas`.
- `src/utils/__init__.py`: Archivo destinado a contener utilidades adicionales en el futuro.
- `requirements.txt`: Lista las dependencias necesarias para ejecutar el proyecto.

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener `pip` instalado y ejecuta el siguiente comando en la raíz del proyecto:

```bash
pip install -r requirements.txt
```

## Uso

Para utilizar el programa, ejecuta el archivo `citaspsiquiatria.py` en un entorno de Python. Asegúrate de tener acceso a Internet para que las solicitudes HTTP funcionen correctamente.

```python
# Ejemplo de uso
from src.citaspsiquiatria import obtener_citas

id_centros = [2552, 2553, 2546]  # IDs de los centros a consultar
citas = obtener_citas(id_centros)
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un issue o un pull request.

## Pruebas unitarias

Este proyecto utiliza [pytest](https://docs.pytest.org/) para las pruebas unitarias.

### Instalación de dependencias para testing

Asegúrate de tener `pytest` instalado. Puedes instalarlo con:

```bash
pip install pytest
```

### Ejecución de los tests

Desde la raíz del proyecto, ejecuta:

```bash
python -m pytest
```

Esto buscará automáticamente todos los archivos que comiencen por `test_` y ejecutará las funciones de prueba.

### Ejemplo de archivo de test

```python
from src.citaspsiquatra import filtrar_citas

def test_filtrar_citas_simple():
    texto = "Lunes, 1 enero 2025 10:00 horas - Hospital X"
    resultado = filtrar_citas(texto)
    assert resultado == [('Lunes', '1 enero 2025', '10:00')]
```

Si todas las pruebas pasan, verás un mensaje indicando que los tests fueron exitosos.