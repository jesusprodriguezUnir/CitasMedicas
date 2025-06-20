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